'''
Defining the coding schemes and other common methods in here so that they 
can more easily be exported to other files.
'''
import os
import numpy as np
import pandas as pd

# Repeat chunking for single + optionally multicolor and nested repeats
def find_repeats(seq, length): 
    """
    Finds repeats of patterns of a fixed length.
    """
    i = 0
    result = []
    while i < len(seq):
        if i + 2 * length <= len(seq) and seq[i:i+length] == seq[i+length:i+2*length]:
            pattern = seq[i:i+length]
            count = 2
            j = i + 2 * length
            while j + length <= len(seq) and seq[j:j+length] == pattern:
                count += 1
                j += length
            result.append(f'[{pattern}]{count}')
            i = j

        else: # move onto the next character
            result.append(seq[i])
            i += 1

    return ''.join(result)

def repeat_chunking(seq, single_only=False): 
    '''
    Finds repeating patterns within a sequence recursively.
    If single_only, only simple single-character repeats.
    Otherwise, includes multicolor and nested repeats.
    Note: Shorter pattern lengths are chunked first. Once a character is chunked, that chunk cannot be broken.
        E.g. GBGBBB = GBG[B]3, not [GB]2[B]2 because the B's at the end are chunked first.
    '''
    length = 1 # Initialize pattern length
    max_len = 1

    # recursively look for repeating patterns of increasing length
    new_seq = seq
    while length <= max_len:
        new_seq = find_repeats(new_seq, length)
        max_len = 1 if single_only else len(new_seq)//2
        length += 1 # increase length and keep going

    code = ''.join(new_seq)
    code_len = len(code.replace('[', '').replace(']', ''))

    return code_len, code

def simple_repeat_scheme(seq):
    '''
    Args: seq (str): A sequence of characters.
    Returns: the length and code (sequence with chunked single repeats).
    '''
    return repeat_chunking(seq, single_only=True)

def complex_repeat_scheme(seq):
    '''
    Including complex repeats (multi-item and nesting).
    '''
    return repeat_chunking(seq, single_only=False)

def repeat_alternation_scheme(seq):
    seq_r = complex_repeat_scheme(seq)[1]
    result = []
    i = 0
    while i < len(seq_r):
        if seq_r[i] == '[':
            j = i
            while seq_r[j] != ']':
                j += 1
            result.append(seq_r[i:j+1])
            i = j + 1
        else:
            if i+2 < len(seq_r) and seq_r[i] == seq_r[i+2]:
                result.append(f'[{seq_r[i:i+2]}*]')
                i += 3
            else:
                result.append(seq_r[i])
                i += 1
    code = ''.join(result)
    code_len = len(code.replace('[', '').replace(']', '').replace('*', ''))
    return code_len, code

def cycle_rep_alt_scheme(seq, weight_dirs=1):
    result = []
    i = 0
    CW = ''.join(np.tile('YBGR', len(seq)//4 + 1))
    CCW = ''.join(np.tile('RGBY', len(seq)//4 + 1))
    while i < len(seq):
        if seq[i] == '[':
            j = i
            while seq[j] != ']':
                j += 1
            result.append(seq[i:j+1])
            i = j + 1
        else:
            if i + 3 < len(seq) and seq[i:i+3] in CW:
                j = i + 3
                while j < len(seq) and seq[i:j+1] in CW:
                    j += 1
                result.append(f'[{seq[i]}{j-i}+]')
                i = j
            elif i + 3 < len(seq) and seq[i:i+3] in CCW:
                j = i + 3
                while j < len(seq) and seq[i:j+1] in CCW:
                    j += 1
                result.append(f'[{seq[i]}{j-i}-]')
                i = j
            else:
                result.append(seq[i])
                i += 1
    
    seq_c = ''.join(result)
    code = repeat_alternation_scheme(seq_c)[1]
    dir_count = code.count('+') + code.count('-')
    code_len = len(code.replace('[', '').replace(']', '').replace('*', '')) \
                + (weight_dirs - 1)*dir_count
    return code_len, code

def test_coding_scheme(scheme, sequences, answers):
    for i in range(len(sequences)):
        s_idx = i
        sequence = sequences[s_idx]
        print(sequence, answers[s_idx])
        code_len, code = scheme(sequence)
        print(code, code_len)
        if code_len != answers[s_idx]:
            print('^ERROR')

# ----- Methods adapted from LempelZivScheme.ipynb -----

def lempel_ziv_complexity(sequence, return_patterns=False):
    """
    Calculates the Lempel-Ziv complexity of a given sequence using a linear time algorithm as described on Wikipedia.
    Optionally returns the set of unique patterns found in the sequence.

    Args:
        sequence (str): The input sequence, which can be of any finite-sized alphabet.
        return_patterns (bool): If True, function also returns the set of unique patterns found.

    Returns:
        int: The Lempel-Ziv complexity of the sequence.
        set (optional): Set of unique patterns found in the sequence.
    """
    n = len(sequence)  # Total length of the sequence
    i = 0  # Current position in the sequence for comparison
    C = 1  # Initialize complexity count. At least one unique subpattern exists.
    u = 1  # Position marking the start of the new component
    v = 1  # Length of the current component being examined
    vmax = v  # Maximum length of a component found at the current position
    unique_patterns = set()  # Set to store unique patterns

    # Loop until the end of the sequence is reached with the current component
    while u + v <= n:
        # If we are not at the end and characters at positions match, extend the component
        if (i + v < n) and (u + v < n) and (sequence[i + v] == sequence[u + v]):
            v += 1
        else:
            # No match found or end reached, update the maximum component length found so far
            vmax = max(v, vmax)
            # Move the comparison index forward
            i += 1
            # Check if we've tried all starting positions up to u
            if i == u:
                # All starting positions have been tried, increment complexity
                C += 1
                new_pattern = sequence[u : u + vmax]
                unique_patterns.add(new_pattern)
                # Move to next position by the length of the longest component found
                u += vmax
                # Reset component length and starting index
                v = 1
                i = 0
                vmax = v
            else:
                # Reset component length to 1 to try a new starting position
                v = 1

    # After exiting the loop, if a component was being built, it's considered a unique pattern
    if v != 1:
        C += 1
        new_pattern = sequence[u : u + v - 1]
        unique_patterns.add(new_pattern)

    if return_patterns:
        return C, unique_patterns
    return C

def LZ_scheme(seq):
    '''
    Calculate the Lempel-Ziv complexity of a sequence.
    '''
    return lempel_ziv_complexity(seq, return_patterns=True)

def parse_simon_game_csv(filepath):
    # Parse the CSV file and convert the color names to single characters
    dataframe = pd.read_csv(filepath)
    dataframe["Event"] = dataframe["Event"].map(
        {"red": "R", "blue": "B", "green": "G", "yellow": "Y", np.nan: "",
         "None": ""}
    )
    # Because there may be multiple gameplays in a single file,
    # we need to split the data frame whenever Score reset to 0.
    # Create a group id that increments each time Score is 0
    dataframe["group_id"] = (dataframe["Score"] == 0).cumsum()
    # Split the data into subdataframes based on group_id
    subdataframes = [group for _, group in dataframe.groupby("group_id")]
    game_results = dict()
    for data in subdataframes:
        # Get the longest chain the player was able to reproduce
        # and the chain they made when they made a mistake.
        best_and_last = data[data.Score >= max(data.Score) - 1]
        # print(best_and_last)
        longest_sequence = "".join(
            best_and_last[
                best_and_last.Score == best_and_last.iloc[0].Score
            ].Event.to_list()
        )
        mistake_sequence = "".join(
            best_and_last[
                best_and_last.Score == best_and_last.iloc[-1].Score
            ].Event.to_list()
        )
        # Discard only length-0 sequences as a result of player inattention.
        if len(longest_sequence) == 0:
            continue
        game_number = data.iloc[0].group_id
        # Dictionary containing the longest sequence and the mistake sequence
        game_sequences = {
            "longest_sequence": longest_sequence,
            "mistake_sequence": mistake_sequence,
        }
        game_results[game_number] = game_sequences
    return game_results

def parse_simons_game_logs(directory):
    session_data = {}
    # Traverse the directory tree
    for root, dirs, files in os.walk(directory):
        # Get all CSV files in the specified directory
        for file in files:
            if file.endswith(".csv"):
                filepath = os.path.join(root, file)
                filename = os.path.basename(filepath)
                game_sequences = parse_simon_game_csv(filepath)
                session_data[filename] = (
                    game_sequences
                )
    return session_data

# ------------------------------------------------------

def generate_random_sequence(length=30, min=None):
    '''
    Generates a random sequence of a specified length.
    '''
    sz = np.random.randint(min, length+1) if min is not None else length

    sequence = "".join(
        np.random.choice(["B", "G", "R", "Y"], size=sz)
    )
    return sequence

def sample_random_sequences(length=30, num_samples=1000, min=None):
    '''
    Generates a list of random sequences.
    '''
    return [generate_random_sequence(length=length, min=min) for _ in range(num_samples)]

def sample_compressed_lengths(scheme, length, num_samples=1000):

    compressed_lengths = []
    for _ in range(num_samples):
        sequence = generate_random_sequence(length=length)
        compressed_lengths.append(scheme(sequence)[0])

    return np.array(compressed_lengths)