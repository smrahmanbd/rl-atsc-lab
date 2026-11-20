# Literature brief: RL-based traffic signal control

*Module: Reinforcement Learning for Adaptive Traffic Signal Control (CE677). Compiled 20 November 2026.*

**How this was checked.** Title, authors, year and venue of every entry were checked against a live source page (the arXiv abstract page, the publisher or the proceedings). Most entries were verified on 30 October 2026 for the Agentic ATSC lab and are reused here; Traffic-R1, LATS, DGLight, MA2C, the Wei et al. survey and IntelliLight were checked on 20 November 2026. When a page names no venue the entry says arXiv preprint, even if the paper has since been published elsewhere. Contribution sentences paraphrase the abstract. Quantitative results are given only where the paper states them. Citation keys match the `id` field in `references.json`.

**Three foundation references** (Sutton and Barto 2018; Watkins and Dayan 1992; Mnih et al. 2015) are standard and are cited from their well-known bibliographic details.

## References

### Foundations

1. **[watkins1992qlearning]** Christopher J. C. H. Watkins, Peter Dayan (1992). *Q-learning*. Machine Learning 8, 279-292. <https://doi.org/10.1007/BF00992698>  
   *Contribution:* Introduces and proves convergence of the Q-learning update used in the Foundation level.
2. **[mnih2015dqn]** Volodymyr Mnih and 18 co-authors (2015). *Human-level control through deep reinforcement learning*. Nature 518, 529-533. <https://doi.org/10.1038/nature14236>  
   *Contribution:* The Deep Q-Network: a neural network in place of the Q-table, made stable with replay memory and a target network.
3. **[sutton2018rlbook]** Richard S. Sutton, Andrew G. Barto (2018). *Reinforcement Learning: An Introduction (2nd edition)*. MIT Press. <http://incompleteideas.net/book/the-book-2nd.html>  
   *Contribution:* The standard textbook: agents, rewards, value functions, temporal-difference learning, Q-learning and function approximation.

### Max-pressure control

4. **[varaiya2013maxpressure]** Pravin Varaiya (2013). *Max pressure control of a network of signalized intersections*. Transportation Research Part C: Emerging Technologies (2013). <https://doi.org/10.1016/j.trc.2013.08.014>  
   *Contribution:* Introduces max-pressure control for signalized networks: a decentralized policy using only local queue information with a proven maximum-throughput (queue-stability) property.
5. **[levin2023mpreview]** Michael W. Levin (2023). *Max-Pressure Traffic Signal Timing: A Summary of Methodological and Experimental Results*. Journal of Transportation Engineering, Part A: Systems, 149(4). <https://ascelibrary.com/doi/10.1061/JTEPBS.TEENG-7578>  
   *Contribution:* State-of-the-art review of max-pressure variants (cycle-based, realistic flow models, measurement error, multimodal access) and their simulation and early field evidence.
6. **[stern2024mndot]** Raphael Stern, Michael W. Levin, Amir Kiani (2024). *Toward Implementation of Max-Pressure Control on Minnesota Roads: Phase 2*. Minnesota Department of Transportation, Report MN 2024-26. <https://rosap.ntl.bts.gov/view/dot/79015>  
   *Contribution:* Hardware-in-the-loop testbed running max-pressure on a Q-Free MaxTime controller, showing MP can be safely deployed on North American signal hardware.

### RL methods

7. **[wei2018intellilight]** Hua Wei, Guanjie Zheng, Huaxiu Yao, Zhenhui Li (2018). *IntelliLight: A Reinforcement Learning Approach for Intelligent Traffic Light Control*. Proc. 24th ACM SIGKDD Int. Conf. on Knowledge Discovery & Data Mining (KDD 2018). <https://faculty.ist.psu.edu/jessieli/Publications/2018-KDD-IntelliLight.pdf>  
   *Contribution:* An early deep RL signal controller tested with real camera-derived traffic data, with attention to interpreting the learned policy.
8. **[chu2019ma2c]** Tianshu Chu, Jie Wang, Lara Codeca, Zhaojian Li (2019). *Multi-Agent Deep Reinforcement Learning for Large-scale Traffic Signal Control*. arXiv preprint arXiv:1903.04527. <https://arxiv.org/abs/1903.04527>  
   *Contribution:* A decentralised multi-agent advantage actor-critic (MA2C) for adaptive signal control, with two techniques that let each local agent see more of its surroundings and learn more easily.
9. **[wei2019colight]** Hua Wei, Nan Xu, Huichu Zhang, Guanjie Zheng, Xinshi Zang, Chacha Chen, Weinan Zhang, Yanmin Zhu, Kai Xu, Zhenhui Li (2019). *CoLight: Learning Network-level Cooperation for Traffic Signal Control*. Proc. 28th ACM Int. Conf. on Information and Knowledge Management (CIKM 2019); arXiv:1905.05717. <https://doi.org/10.1145/3357384.3357902>  
   *Contribution:* Uses graph attention so neighbouring signal agents communicate and coordinate, reported to outperform state-of-the-art methods on a network with hundreds of signals.
10. **[wei2019presslight]** Hua Wei, Chacha Chen, Guanjie Zheng, Kan Wu, Vikash Gayah, Kai Xu, Zhenhui Li (2019). *PressLight: Learning Max Pressure Control to Coordinate Traffic Signals in Arterial Network*. Proc. 25th ACM SIGKDD Int. Conf. on Knowledge Discovery & Data Mining (KDD 2019), pp. 1290-1298. <https://doi.org/10.1145/3292500.3330949>  
   *Contribution:* Grounds the RL reward in max-pressure theory (linked to throughput maximisation) with a compact state, outperforming conventional and prior learning-based controllers on arterials.
11. **[zheng2019frap]** Guanjie Zheng, Yuanhao Xiong, Xinshi Zang, Jie Feng, Hua Wei, Huichu Zhang, Yong Li, Kai Xu, Zhenhui Li (2019). *Learning Phase Competition for Traffic Signal Control*. Proc. 28th ACM Int. Conf. on Information and Knowledge Management (CIKM 2019), pp. 1963-1972. <https://doi.org/10.1145/3357384.3357900>  
   *Contribution:* FRAP models competition between phases by demand, giving invariance to flips/rotations, faster convergence and better generalisation across intersection structures.
12. **[chen2020mplight]** Chacha Chen, Hua Wei, Nan Xu, Guanjie Zheng, Ming Yang, Yuanhao Xiong, Kai Xu, Zhenhui Li (2020). *Toward A Thousand Lights: Decentralized Deep Reinforcement Learning for Large-Scale Traffic Signal Control*. Proc. AAAI Conference on Artificial Intelligence, 34(04), 3414-3421. <https://doi.org/10.1609/aaai.v34i04.5744>  
   *Contribution:* MPLight: decentralized deep RL using pressure-based regional coordination and a reward that lets agents coordinate implicitly, demonstrated on a real-world Manhattan network of 2,510 traffic lights.
13. **[oroojlooy2020attendlight]** Afshin Oroojlooy, Mohammadreza Nazari, Davood Hajinezhad, Jorge Silva (2020). *AttendLight: Universal Attention-Based Reinforcement Learning Model for Traffic Signal Control*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020). <https://papers.nips.cc/paper/2020/hash/29e48b79ae6fc68e9b6480b677453586-Abstract.html>  
   *Contribution:* A single attention-based policy that handles intersections with different numbers of roads, lanes and phases without retraining, outperforming classical and RL baselines in single- and multi-environment regimes.
14. **[wu2021efficientxlight]** Qiang Wu, Liang Zhang, Jun Shen, Linyuan Lü, Bo Du, Jianqing Wu (2021). *Efficient Pressure: Improving efficiency for signalized intersections*. arXiv preprint arXiv:2112.02336. <https://arxiv.org/abs/2112.02336>  
   *Contribution:* Introduces efficient pressure (EP) and builds Efficient-MP and the Efficient-XLight RL family, evaluated on multiple real-world datasets.

### Simulators and benchmarks

15. **[lopez2018sumo]** Pablo Alvarez Lopez, Michael Behrisch, Laura Bieker-Walz, Jakob Erdmann, Yun-Pang Flötteröd, Robert Hilbrich, Leonhard Lücken, Johannes Rummel, Peter Wagner, Evamarie Wießner (2018). *Microscopic Traffic Simulation using SUMO*. 21st IEEE Int. Conf. on Intelligent Transportation Systems (ITSC 2018), pp. 2575-2582. <https://doi.org/10.1109/ITSC.2018.8569938>  
   *Contribution:* Reference description of the open-source SUMO microscopic simulator widely used for TSC, V2X and CAV studies.
16. **[alegre2019sumorl]** Lucas N. Alegre (2019). *SUMO-RL*. GitHub repository (software). <https://github.com/LucasAlegre/sumo-rl>  
   *Contribution:* Gymnasium/PettingZoo-compatible RL environments for traffic signal control on top of SUMO.
17. **[zhang2019cityflow]** Huichu Zhang, Siyuan Feng, Chang Liu, Yaoyao Ding, Yichen Zhu, Zihan Zhou, Weinan Zhang, Yong Yu, Haiming Jin, Zhenhui Li (2019). *CityFlow: A Multi-Agent Reinforcement Learning Environment for Large Scale City Traffic Scenario*. The World Wide Web Conference (WWW 2019); arXiv:1905.05217. <https://doi.org/10.1145/3308558.3314139>  
   *Contribution:* A fast, scalable microscopic simulator for city-scale multi-agent RL, the default platform for most PressLight/CoLight/LLMLight-family studies.
18. **[ault2021resco]** James Ault, Guni Sharon (2021). *Reinforcement Learning Benchmarks for Traffic Signal Control*. Proc. NeurIPS Track on Datasets and Benchmarks, Vol. 1 (2021). <https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/f0935e4cd5920aa6c7c996a5ee53a70f-Abstract-round1.html>  
   *Contribution:* RESCO toolkit and realistic SUMO benchmark scenarios; finds earlier methods are brittle to changed sensing assumptions and irregular intersections.
19. **[muller2021lemgorl]** Arthur Müller, Vishal Rangras, Georg Schnittker, Michael Waldmann, Maxim Friesen, Tobias Ferfers, Lukas Schreckenberg, Florian Hufen, Jürgen Jasperneite, Marco Wiering (2021). *Towards Real-World Deployment of Reinforcement Learning for Traffic Signal Control*. 20th IEEE Int. Conf. on Machine Learning and Applications (ICMLA 2021), DOI 10.1109/ICMLA52953.2021.00085; arXiv:2103.16223. <https://arxiv.org/abs/2103.16223>  
   *Contribution:* LemgoRL: a realistic benchmark of the German town of Lemgo with a signal-logic unit enforcing regulatory and safety constraints, aimed at deployable RL.
20. **[mei2023libsignal]** Hao Mei, Xiaoliang Lei, Longchao Da, Bin Shi, Hua Wei (2023). *LibSignal: An Open Library for Traffic Signal Control*. Machine Learning (Springer), DOI 10.1007/s10994-023-06412-y; arXiv:2211.10649. <https://arxiv.org/abs/2211.10649>  
   *Contribution:* Open library benchmarking RL-TSC models across both SUMO and CityFlow with calibrated environments and shared protocols.

### Evidence on the gaps

21. **[ault2020interpretable]** James Ault, Josiah P. Hanna, Guni Sharon (2020). *Learning an Interpretable Traffic Signal Control Policy*. arXiv preprint arXiv:1912.11023. <https://arxiv.org/abs/1912.11023>  
   *Contribution:* Learns regulatable polynomial (interpretable) signal policies via modified Deep Q-learning, reducing delay up to 19.4% vs. actuated control while remaining inspectable.
22. **[da2023ugat]** Longchao Da, Hao Mei, Romir Sharma, Hua Wei (2023). *Uncertainty-aware Grounded Action Transformation towards Sim-to-Real Transfer for Traffic Signal Control*. arXiv preprint arXiv:2307.12388. <https://arxiv.org/abs/2307.12388>  
   *Contribution:* UGAT applies grounded action transformation only when its uncertainty is low, narrowing the transition-dynamics gap between simulator and target environment for RL-TSC.
23. **[du2023safelight]** Wenlu Du, Junyi Ye, Jingyi Gu, Jing Li, Hua Wei, Guiling Wang (2023). *SafeLight: A Reinforcement Learning Method toward Collision-free Traffic Signal Control*. Proc. AAAI Conference on Artificial Intelligence, 37(12), 14801-14810. <https://doi.org/10.1609/aaai.v37i12.26729>  
   *Contribution:* Safety-enhanced residual RL with multi-objective loss and reward shaping based on road-safety standards, significantly reducing collisions while improving mobility.
24. **[mei2023missingdata]** Hao Mei, Junxian Li, Bin Shi, Hua Wei (2023). *Reinforcement Learning Approaches for Traffic Signal Control under Missing Data*. Proc. 32nd Int. Joint Conf. on Artificial Intelligence (IJCAI 2023), DOI 10.24963/ijcai.2023/251. <https://arxiv.org/abs/2304.10722>  
   *Contribution:* Imputes missing states (and rewards) so RL controllers keep working at intersections without sensors, staying robust across missing-data rates.
25. **[kwesiga2026robustness]** Dickens Kwesiga, Angshuman Guin, Khaled Abdelghany, Michael Hunter (2026). *Evaluating the Robustness of Reinforcement Learning based Adaptive Traffic Signal Control*. arXiv preprint arXiv:2603.15283. <https://arxiv.org/abs/2603.15283>  
   *Contribution:* RL controller with field-realistic eight-phase ring-barrier structure cuts delay 11-32% vs. optimised actuated control but degrades under substantially different O-D demand unless trained on diverse patterns.
26. **[rafi2026sim2signal]** Ferdous Al Rafi, Susrik Mukherjee, Latika Liladhar Dekate, Jennifer Yawa Lavoe, Huaiyuan Yao, Shlok Mohanty, Longchao Da, Xuesong Zhou, Hua Wei (2026). *Sim2Signal: Sim-to-Real Benchmarks for Traffic Signal Control*. arXiv preprint arXiv:2609.01676. <https://arxiv.org/abs/2609.01676>  
   *Contribution:* Decomposes the sim-to-real gap into observation, action, transition and reward gaps and tests 18 mitigation methods over 33 gap settings and 10 calibrated networks; direct transfer always degrades and no mitigation wins everywhere.
27. **[zhang2026equity]** Xiaocai Zhang, Neema Nassir, Lok Sang Chan, Milad Haghani (2026). *Human-Centric Traffic Signal Control for Equity: A Multi-Agent Action Branching Deep Reinforcement Learning Approach*. arXiv preprint arXiv:2602.02959. <https://arxiv.org/abs/2602.02959>  
   *Contribution:* MA2B-DDQN rewards minimising the number of delayed people (pedestrians, occupants, transit riders) on a Melbourne corridor, shifting TSC objectives from vehicles to travellers.

### Language models with RL

28. **[da2024promptgat]** Longchao Da, Minquan Gao, Hao Mei, Hua Wei (2024). *Prompt to Transfer: Sim-to-Real Transfer for Traffic Signal Control with Prompt Learning*. Proc. AAAI Conference on Artificial Intelligence (AAAI 2024); arXiv:2308.14284. <https://ojs.aaai.org/index.php/AAAI/article/view/27758>  
   *Contribution:* PromptGAT uses LLM cloze-style prompts to infer how weather, road type and traffic state alter system dynamics, then grounds a DQN agent's actions to those dynamics, narrowing the sim-to-real performance gap.
29. **[pang2024illmtsc]** Aoyu Pang, Maonan Wang, Man-On Pun, Chung Shue Chen, Xi Xiong (2024). *iLLM-TSC: Integration reinforcement learning and large language model for traffic signal control policy improvement*. arXiv preprint arXiv:2407.06025. <https://arxiv.org/abs/2407.06025>  
   *Contribution:* LLM-assisted RL: an RL agent proposes the phase and an LLM checks and corrects unreasonable decisions (degraded communication, rare events such as emergency vehicles), reducing average waiting time by 17.5% vs. RL alone under degraded communication.
30. **[wang2024lalight]** Maonan Wang, Aoyu Pang, Yuheng Kan, Man-On Pun, Chung Shue Chen, Bo Huang (2024). *LLM-Assisted Light: Leveraging Large Language Model Capabilities for Human-Mimetic Traffic Signal Control in Complex Urban Environments*. arXiv preprint arXiv:2403.08337. <https://arxiv.org/abs/2403.08337>  
   *Contribution:* LA-Light places an LLM at the centre of control and gives it perception and decision tools (static/dynamic traffic queries, existing TSC algorithms); in the authors' simulation platform it adapts without retraining and cuts average waiting time by 20.4% vs. RL controllers under sensor-outage conditions.
31. **[lai2025llmlight]** Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, Hui Xiong (2025). *LLMLight: Large Language Models as Traffic Signal Control Agents*. Proc. ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 2025); arXiv:2312.16044. <https://arxiv.org/abs/2312.16044>  
   *Contribution:* Uses an LLM as the signal-control agent, prompted with real-time traffic state and reasoning step by step, plus LightGPT, a backbone fine-tuned for TSC; on ten real and synthetic datasets it is reported to beat nine traditional/RL baselines and ten general LLMs, with interpretability rated by fifteen human experts.
32. **[zou2025trafficr1]** Xingchen Zou, Yuhao Yang, Zheng Chen, Xixuan Hao, Yiqi Chen, Chao Huang, Yuxuan Liang (2025). *Traffic-R1: Reinforced LLMs Bring Human-Like Reasoning to Traffic Signal Control Systems*. arXiv preprint arXiv:2508.02344. <https://arxiv.org/abs/2508.02344>  
   *Contribution:* A 3-billion-parameter language model trained with offline then online RL for signal control; reports a six-week A/B test at 10 intersections in a Chinese city with a reduction in average queue length of roughly 9% against manual control.
33. **[yu2026dglight]** Chenbo Yu (2026). *DGLight: DQN-Guided GRPO Fine-Tuning of Large Language Models for Traffic Signal Control*. arXiv preprint arXiv:2604.25259. <https://arxiv.org/abs/2604.25259>  
   *Contribution:* Uses a frozen CoLight-based Deep Q-Network as a critic that scores a language model's candidate actions, and trains the language model on those scores.
34. **[yuan2026collmlight]** Zirui Yuan, Siqi Lai, Hao Liu (2026). *CoLLMLight: Cooperative Large Language Model Agents for Network-Wide Traffic Signal Control*. International Conference on Learning Representations (ICLR 2026); arXiv:2503.11739. <https://arxiv.org/abs/2503.11739>  
   *Contribution:* Network-level cooperative LLM agents using a spatiotemporal graph of neighbouring intersections, complexity-aware reasoning depth and simulation-feedback fine-tuning of a lightweight LLM; reported to outperform state-of-the-art methods on synthetic and real datasets.
35. **[zhang2026lats]** Yifeng Zhang, Peizhuo Li, Tingguang Zhou, Mingfeng Fan, Guillaume Sartoretti (2026). *LATS: Large Language Model Assisted Teacher-Student Framework for Multi-Agent Reinforcement Learning in Traffic Signal Control*. arXiv preprint arXiv:2603.24361. <https://arxiv.org/abs/2603.24361>  
   *Contribution:* A language model acts as teacher, producing features that describe each intersection; a small student network learns to reproduce them, so the final RL controller runs without the language model.

### Surveys

36. **[wei2019survey]** Hua Wei, Guanjie Zheng, Vikash Gayah, Zhenhui Li (2019). *A Survey on Traffic Signal Control Methods*. arXiv preprint arXiv:1904.08117. <https://arxiv.org/abs/1904.08117>  
   *Contribution:* Reviews conventional transportation approaches to signal control alongside reinforcement learning studies, to encourage work across the two fields.
37. **[zhang2024rlcavsurvey]** Kaiwen Zhang, Zhiyong Cui, Wanjing Ma (2024). *A survey on reinforcement learning-based control for signalized intersections with connected automated vehicles*. Transport Reviews, 44(6), 1187-1208. <https://doi.org/10.1080/01441647.2024.2377637>  
   *Contribution:* Systematic review of RL for CV/CAV-data signal control, RL trajectory planning for CAVs and cooperative signal-CAV control, with a research roadmap.

## Gaps

| Gap | What goes wrong | Evidence | Directions |
|---|---|---|---|
| Sim-to-real | Simulated drivers, detectors and signals differ from real ones | Direct transfer degraded in every setting tested [rafi2026sim2signal] | Grounded action transformation [da2023ugat]; prompt-based grounding [da2024promptgat]; realistic benchmarks [muller2021lemgorl] |
| Robustness | Traffic differs from training | Single-pattern training degrades under different demand [kwesiga2026robustness]; earlier methods brittle [ault2021resco] | Train on varied demand; stress tests |
| Safety | The agent proposes an unsafe or illegal change | Road-safety standards built into RL reduce collisions [du2023safelight]; regulatory logic unit [muller2021lemgorl] | Rule layer outside the agent; action masking |
| Missing data | Detectors fail | Imputation keeps control working [mei2023missingdata]; 20.4% gain under sensor outage reported [wang2024lalight] | Imputation; fallback reviewers |
| Explainability | Operators cannot see why a phase was chosen | Inspectable policy, up to 19.4% less delay than actuated [ault2020interpretable]; rationales rated by 15 experts [lai2025llmlight] | Simple policy forms; checked explanations |
| Fairness | Vehicle throughput ignores people | People-based reward on a Melbourne corridor [zhang2026equity] | People-based rewards; maximum-wait limits |
| Deployment | No route from paper to controller cabinet | Hardware-in-the-loop max-pressure [stern2024mndot]; six-week field A/B test at 10 intersections [zou2025trafficr1] | Hardware-in-the-loop, shadow mode, staged trials |

## Eight research ideas

1. **Unseen traffic (starter).** Train on one demand pattern and on a mix; test both on unseen patterns. Read [kwesiga2026robustness], [ault2021resco].
2. **Reward shoot-out (starter).** Same agent, three rewards: queue, waiting time, pressure. Read [wei2019presslight], [wu2021efficientxlight].
3. **Safety shield (starter).** Add minimum green and maximum wait as an override layer; measure the delay cost and the override count. Read [du2023safelight], [muller2021lemgorl].
4. **Detector failure (intermediate).** Blank one approach's reading 10%, 30% and 50% of the time at test. Read [mei2023missingdata], [wang2024lalight].
5. **People, not vehicles (intermediate).** Add buses and a pedestrian phase; compare vehicle-based and people-based rewards. Read [zhang2026equity], [levin2023mpreview].
6. **Sim-to-real for one parameter (intermediate).** Train with default driver settings; test with slower reactions and gentler acceleration. Read [da2023ugat], [rafi2026sim2signal].
7. **Readable rules (intermediate).** Fit a small table or decision tree to a trained DQN. Read [ault2020interpretable].
8. **Language model helper (advanced).** Let a language model review only unusual states. Read [pang2024illmtsc], [zhang2026lats], [yu2026dglight].

## Notes on what was not verified

- The MA2C paper (Chu et al.) and the Wei et al. survey are cited as arXiv preprints because their arXiv pages list no journal reference.
- For Traffic-R1 the abstract and the introduction give slightly different queue-reduction figures; this module therefore says roughly 9% for average queue length.
- The abstract pages for LATS and DGLight give no numerical results, so none are quoted.
