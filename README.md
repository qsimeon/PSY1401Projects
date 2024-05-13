# PSY1401Projects
Github repository to collaborate on class projects for PSY1401 taught by Professor Sam Gershman.

## Group Project Repository
Welcome to our group project repository! Here, we collaborate on various projects, each with its own dedicated Google Colab notebook for ease of use and real-time collaboration.

## Contact
For any queries or assistance, please reach out to the team members via our communication channels.

- [**Slack**](https://mit.enterprise.slack.com/archives/C06FNKK4MRD)

- **Emails**
  - [Sol Markman](smarkman@MIT.EDU)
  - [Hokyung Sung](hokyung@MIT.EDU)
  - [Quilee Simeon](qsimeon@MIT.EDU)
  - [Jack Gabel](gabel@MIT.EDU)

---

## Projects

### Project 1: Normalization as a canonical neural computation

#### Description:
1) Implement the normalization function (Equation 10 in Carandini & Heeger, 2012) and show how this function removes redundancy in an input (i.e., by decorrelating the pixels).

2) Show how the normalization function induces winner-take-all competition in a population of neurons tuned to different orientations (see Figure 3e in Carandini & Heeger, 2012).

3) Implement the adaptation version of normalization (Equation 12 in Carandini & Heeger, 2012) and show how this produces light adaptation in the retina.

4) Discuss the empirical evidence for normalization in the visual system.

5) Discuss the possible biological mechanisms that could give rise to normalization.

#### References: 
Carandini, M. & Heeger, D.J. (2012). Normalization as a canonical neural operation. Nature Reviews Neuroscience, 13, 51-62.

#### Files:
- [Project 1 Notebook](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/Notebook%201-722cb16dd39448d58a75ce12268e6ff6)

- [Project 1 Slides](https://docs.google.com/presentation/d/1U3EmTjXoUij8sFbSxL47A_2-dvUX-xZlMLf4rQBUs40/edit?usp=sharing)

#### Assessment:
Great talk today! I thought you did a great job demonstrating the effects of normalization through multiple simulations. 

**What worked great:**
- The simulations were nicely done and highly effective in showing how the normalization function reduces redundancy, induces winner-take-all competition, and produces light adaptation in the retina.

- I like how you managed to go deeper into the math while keeping people focused on the big picture.

**Some advice for next time:**
- Try focusing more on motivating the problem and illustrating the big picture. Ironically, it’s the simulations that take us the greatest time to create, but it’s the high-level descriptions that often stick with the audience. For example, why even care about normalization? How does this relate to the real world?

**Grade:** A

---

### Project 2: Modeling an adaptive learning rate

#### Description: 
1) Implement the version of the Pearce-Hall model as described in Li et al. (2011; see their supplementary materials). Show how this model results in a faster learning rate when rewards are more volatile (see Behrens et al., 2007). Compare this model to the standard Rescorla-Wagner model, which lacks an adaptive learning rate.

2) What happens to the learning rate and value after increases/decreases in positive and/or negative prediction errors? How can these two signals be distinguished experimentally?

3) Discuss the neural and behavioral evidence for adaptive learning rate (see Roesch et al., 2011).

#### References: 
* Behrens, T.E., Woolrich, M.W., Walton, M.E. & Rushworth, M.F. (2007) Learning the value of information in an uncertain world. Nature Neuroscience, 10, 1214–1221.

* Li, J., Schiller, D., Schoenbaum, G., Phelps, E.A., & Daw, N.D. (2011). Differential roles of human striatum and amygdala in associative learning. Nature Neuroscience, 14, 1250–1252.

* Roesch, M.R., Esber, G.R., Li, J., Daw, N.D., and Schoenbaum, G. (2012). Surprise! Neural correlates of Pearce-Hall and Rescorla-Wagner coexist within the brain. European Journal of Neuroscience, 35, 1190–1200.

#### Files:
- [Project 2 Notebook](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/PSY1401%20Project%202-71e832ab19774a2aa519ad23f5390365)

- [Project 2 Slides](https://docs.google.com/presentation/d/1jIn6BOZ8RuSJ5woJKP6MNJXRxUE5tWgXFtrjeaRA-os/edit?usp=sharing)

#### Assessment:
Nice job on your presentation about the Pearce-Hall model today! Keep up the good work!

**What worked great:**
- I thought you did a great job presenting the conceptual differences between the RW and PH models. 

- You ran exactly the right simulations, thoughtfully walked us through your reasoning and analysis of the simulations, and provided quite the tour de force with your review of behavioral/neural evidence.

**Some advice for next time:**
- It would be nice if you could motivate the model, for example in this particular case, why do we need an adaptive learning rate in the first place, what kinds of situations would the RW model fail to address that motivate a variable learning rate? Relatedly, I think Ho's (let me know if I should call you Hokyung or Ho) proposal of a distribution of learning rates is very interesting, and I'd love to see more of that critical thinking about the models and theories in future presentations (although not a must)! 

**Grade:** A

---

### Project 3: Exploration/Exploitation

#### Description: 
1) Jepma \& Nieuwenhuis (2011) have presented evidence from pupillary measurements that norepinephrine is related to the balance between exploration and exploitation. In particular, they suggest that uncertainty might be signaled by tonic norepinephrine (as measured by baseline pupil diameter), and that this signal predicts the shift from exploration to exploitation. A simple way to track this uncertainty (see Frank et al., 2009) is using a Bayesian model of the reward distribution for each option. Specifically, each option is associated with an unknown reward probability; the learner represents their belief about this reward probability using a beta $(a, b)$ distribution. When $a=b=1$ at the beginning of learning, the distribution is uniform over all possible reward probabilities. Whenever a reward is observed, $a^{\prime}=a+1$, and whenever a reward is not observed, $b^{\prime}=b+1$. Assume that each option $i$ is assigned a decision value according to: $Q(i)=M(i)+\sigma^* V(i)$
Where $M(i)=a /(a+b)$ is the expected reward probability, and $\mathrm{V}(\mathrm{i})=\left(\mathrm{a}^* \mathrm{~b}\right) /\left[(\mathrm{a}+\mathrm{b})^{2 *}(\mathrm{a}+\mathrm{b}+1)\right]$ is the variance of the beta distribution, playing the role of an "uncertainty bonus" weighted by parameter $\sigma$. Assume that actions are chosen according to a softmax policy: $P(i)=\exp (\beta * Q(i)) / \sum_j \exp (\beta * Q(j))$. Show how this model can account for the relationship between pupil diameter and exploration/exploitation under the assumption that baseline pupil diameter is proportional to the entropy of the distribution over actions.

2) What happens when you don't have the uncertainty bonus? How could you experimentally determine whether or not people use an uncertainty bonus?

3) Discuss how this model could be related to dopaminergic novelty bonuses (Kakade \& Dayan, 2002).

#### References:
* Cohen, J.D., McClure, S.M., & Yu, A. J. (2007). Should I stay or should I go? Exploration versus exploitation. Philosophical Transactions of the Royal Society B, 362, 933-942.

* Frank, M. J., Doll, B. B., Oas-Terpstra, J., & Moreno, F. (2009). Prefrontal and striatal dopaminergic genes predict individual differences in exploration and exploitation. Nature Neuroscience, 12, 1062–1068.

* Kakade, S. & Dayan, P. (2002). Dopamine: generalization and bonuses. Neural Networks, 15, 549–559.

#### Files:
- [Project 3 Notebook](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/PSY1401%20Project%203-a3375a3d116b4735ac79296b88f515a1)

- [Project 3 Slides](https://docs.google.com/presentation/d/1XfCAcN920nGDGkh2g4__XbU_fELh6UvE6OGFpEjOnIw/edit?usp=sharing)

#### Assessment:
Great presentation on exploration/exploitation today! Very well done!

**What worked great:**
- There were a lot of things to love about your presentation, for example I liked Jack’s lead-in and introduction, Quilee’s explanation of the model details and walk-through of the very nice simulation, Sol’s simulation of what would happen if we get rid of the uncertainty bonus and the proposed experimental design to test if participants actually use an uncertainty bonus, and Hokyung’s simulation and discussion of the novelty bonus and relating that to the uncertainty bonus.

- I think all of your presentations have been amazing, and this one in particular stands out as being coherent and well-rounded. I especially liked the discussions about novelty bonus and uncertainty bonus, lots of interesting ideas shined through, and I think these are what makes a presentation beyond a summary of what you have done and what others have done, so that was really wonderful!

**Some advice for next time:**
- Having some more high-level discussions around these effects would be helpful. For example, what kind of needs might be motivating the novelty bonus in the first place?

**Grade:** A

---

### Project 4: Memory in context

#### Description: 
1) Implement the temporal context model described by Manning et al. (2011) and show how it accounts for neural context reinstatement.

2) Test whether the model can explain the findings of Howard et al. (2012).

3) Discuss why neural similarity shows forward-backward symmetry, but the free recall data show an asymmetry. How can the temporal context model account for this?

#### References:
* Howard, M. W., Viskontas, I. V., Shankar, K. H., & Fried, I. (2012). A neural signature of mental time travel in the human MTL. Hippocampus, 22, 1833–1847.

* Manning, J. R., Polyn, S. M., Baltuch, G., Litt, B., & Kahana, M. J. (2011). Oscillatory patterns in temporal lobe reveal context reinstatement during memory search. Proceedings of the National Academy of Sciences, 108, 12893–12897.

#### Files
- [Project 4 Notebook](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/PSY1401%20Project%204-e0ce8aff4f09424fb656006f5d267d1d)

- [Project 4 Slides](https://docs.google.com/presentation/d/1BnsfVn41KCzGFlOYYNqMXfy9yLBtOdKTqaQ4FVq4mk4/edit?usp=sharing)

#### Assessment:
Fantastic talk today! I thought you did a great job presenting the temporal context model. The in-class experiment was definitely interesting and was a good illustration of your main point. Your presentation of the Manning paper and the Howard paper was quite clear, the simulations were spot-on, and the closing discussion about the symmetry in neural similarity and asymmetry in free recall data was great. Congrats on finishing all the mini-project presentations! Looking forward to your final project.

**Grade:** A

---

### Final Project: Chunking in seqeunce learning

#### Proposal:
The Simon game is a popular toy that involves learning a sequence of colors. The game builds up one item at a time and encourages the player to remember as long of a sequence as possible. Humans learn remarkably lengthy sequences in this game, comprising 15+ items for a typical player. We hypothesize that subjects learn such long sequences by compressing the colors into ‘chunks’ like ‘4 x red’ or ‘circular pattern’. In this project, we will first explore a space of behavioral models that characterize how compressible a given sequence is using algorithmic information-theoretic measures (e.g., Kolmogorov complexity given a coding scheme), and use the complexity measure to predict human behavioral performance. We will then collect data from human subjects and use the models to assess (1) if humans perform better with more compressible sequences, and (2) which models best correlate with human accuracies and reaction times. After we discern the compression scheme that best characterizes human behavior, we will formulate neural models (such as RNNs) that explore how the compression scheme may be implemented in the brain. Ultimately, this project may shed light on whether chunking underlies the strong performance of human subjects in the Simon game.

#### Files:
- [Final Project - Neural model](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/Final%20Project%20-%20Neural%20model-a67209bd885e4d59b59f75100d7c054c)

- [Final Project - Sequence code](https://deepnote.com/workspace/default-ae8c-cd19bf13-8f43-4da3-9f0c-aa16e4875ff5/project/PSY-1401-Group-2-3569eb68-a6a6-4122-9c3d-498e88f49235/notebook/Final%20Project%20-%20Sequence%20code-04d5e677233c48e29ae90d1249dda94a)

- [Final Project Slides](https://docs.google.com/presentation/d/1cxtoTaRz4g2p6MoJVFoGEn-B0nWog4YtA60cd3Mkm8s/edit?usp=sharing)

- [Final Project Report](https://docs.google.com/document/d/19QjyL0h_vO2xfzWEqLngsa-ylBaJN68nlAArLXN3e1U/edit?usp=sharing)

#### Assessment:
Thank you for submitting your final project report. You started by motivating the project, explaining why the Simon Game was interesting, and then proposed the chunking hypothesis and reviewed relevant evidence for chunking. Behaviorally, you came up with five coding schemes and tested them in human subjects. Neurally, you formulated three models and simulated them, as hypotheses of what’s going on inside people’s brains when they memorize long sequences.

Overall, this work is awesome! I think the topic is interesting, the writing and technical details were clear, and there was a lot of thinking involved - I liked how you explained your choices of tasks, models, even the normalization in defining chunkability, listing what you tried, why things worked/didn’t work, and how you landed on the final decisions.

I especially liked your idea of chunking being implemented through the firing rates of neurons, where firing rates scale with the number of repeats. This is clever! I also liked the idea of encoding and updating contexts in the CC-STSP model. For the temporal model, my read is that it assumes that four colors need to be looped through before returning to a color that occurred before. Is that right? Because then it wouldn’t be able to apply to sequences like R[3]GBRY where a color (R) shows up a second time after some other colors are shown but before all colors are shown.

The discussions of your results, limitations, and future directions are great. One thing, though, is I think “This work argues that chunking explains our surprisingly lengthy Simon sequences” is a strong conclusion. I did not take your results to mean that chunking explains how people remember long sequences; rather, there seem to be at most some correlations between longer sequences remembered and the chunkability according to a couple, but not all of the coding schemes you tested. There also seems to be a lot of variability across individuals (Figure 10). That said, this is a really nice paper and I enjoyed reading it!

Great work, and thanks for an amazing semester!

**Grade:** A

---