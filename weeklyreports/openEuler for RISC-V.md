# openEuler for RISCV

TL;DR: 会议上来自 wuwei 的一些观点

- 从12月开始应该有几个长期维护的工程（分支）：oE/mainline、oE/2203、oE/2003（或oE/2109），主线分支保持某种形式的CI检测在riscv64上的regression；2203是为下一个版本；2003或2109是为了目前在 RISC-V Lab 等软件所维护的系统中的支持。
- 三个分支（工程）都需要各自从 oE 的统一工程中 branchout/fork。带有 RISC-V 后缀的工程不应该再被 branchout 出来（否则会导致代码源分裂）。
- 三个工程的软件版本等不同，之间的代码关系，既有从 oE/mainline/RISCV 上 backport 到 2203 的情况，也有 2203 单独打特定 patch 的情况。需要根据具体情况来 review。
- 三个工程理论上构建环境（rootfs+种子仓库）可以不一样，或必然不一样（Kernel headers、GCC 和 GLIBC 版本不同）。我们需要开始考虑每个工程（分支）的构建环境的维护。
- 目前的 oE/mainline/RISCV 工程，名字已经不能体现工程的实际情况：截止到11月30日的 oE/mainline/RISCV 分支应该是从 2109 之后的某个 commit 分出来，已经没有百分百跟 mianline 对应：工程的代码仓库来源是 src-openeuler 和 openeuler-riscv 目录下的混合，同时还包含了若干个个人账号下的 repos。 **这在后续需要改变下，将截止到11月30日的 oE/mainline/RISCV 改个名字去掉mainline的字样。（具体操作可以复制一份再改名）
- 不应该有 selfBuild0、1、2 的细分，是不必要的。概念上只需要区分3类包/环境：第0类是用非oE仓库构建出来的rpm包（偷包）组装出来的 rootfs + yum repo，去构建oE仓库中基本的rpm，得到 baseOS0；第1类是用得到的 baseOS， oE代码仓库中各种软件固定好一个基线版本，用 baseOS0 重新构建 baseOS1。第2类是用 baseOS1 构建所有 oE/RV 上的 4000+ 包。注意 baseOS1 和对应的 yum repo 软件可以（应该）是稳定不变的，它对应了（例如）2203版本的第一次正式发布的 rpm 集合。这个 baseline 可以持续构建所有（例如）2203 分支上的软件更新（不然的话就用户运行 yum update 或者 yum install 的时候可能会遇到 dependance conflicts）
- 在2021年12月1日之前的各类决策在当时是合理的，有限人力下只能够维护一个分支；而由于构建系统的速度限制，必须脱离跟 oE/mainline 代码自动更新和OBS构建自动更新（因为更新频度导致的构建所需时间超过了构建系统能力）。而这两条前提都后续都会改变，我们应当开始考虑三个分支维护和逐步跟arm64/x86同一套代码仓库。
- 在2203正式发布之后可以暂停掉2003或2109工程（分支），只维护 mainline 和 2203 两个工程。 2003/2109 工程可以在 2022 年 6 月左右停止更新。
- 以上立项情况发生的前提有三： 第一，OBS构建系统速度足够在24小时内构建4000+个包； 第二，建立被动式的CI检测新代码提交在 RISC-V 平台上的 regression 并及时报警（目前还不太可能作为门禁）； 第三， 有足够的人力和足够经验的工程师即使修复。让我们在12月份先把1和3做到足够好。

## 1. 维护中的分支（现状描述）

1. openEuler RISC-V根据当前的情况，维护以下2个版本：

   （1）openEuler riscv的master：滚动更新

   > 需要确定下：mainline:RISC-V到底是滚动更新的riscv master、还是历史的某一个版本？目前mainline:RISC-V在维护过程中，有些包的版本未更新过，有的更新了，已经无法与上游【系统某版本】对应上。软件包版本问题可能是导致滚动自构建失败的原因。
   >
   >
   >
   > 如果是master的话，要怎么去维护master？
   >
   >

   （2）openEuler 22.03:LTS 分支：固定版本

   > 为openeuler 22.03发布而生成的版本



2. obs构建工程管理

   | 分支      | obs工程                                                      | obs工程名上游                                                |
   | --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | master    | [openEuler:Mainline:RISC-V](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V) | [openEuler:Mainline](https://build.openeuler.org/project/show/openEuler:Mainline) |
   | 22.03:LTS | openEuler:22.03:LTS:Next:RISC-V    (待建)                    | [openEuler:22.03:LTS:Next](https://build.openeuler.org/project/show/openEuler:22.03:LTS:Next) |



3. 源码管理

   | 分支      | 源码仓                                                       | 源码上游                                           |
   | --------- | ------------------------------------------------------------ | -------------------------------------------------- |
   | master    | src-openeuler/packagename/master                             |                                                    |
   |           | openeuler-risc-v/packagename/master                          | src-openeuler/packagename/master                   |
   | 22.03:LTS | src-openeuler/packagename/openEuler-22.03-LTS-Next           |                                                    |
   |           | openeuler-risc-v/packagename/openEuler-22.03-LTS-Next    (待建) | src-openeuler/packagename/openEuler-22.03-LTS-Next |

   备注：

   - 关于源码仓

   > 理论上，源码仓都是src-openeuler/包名/分支名；但是由于在实际构建过程中，代码的提交合入效率会影响构建进度，而且非riscv的其它修改也可能导致riscv构建错误。——》引入了临时中转仓库，用于临时存放riscv的源码修改，待在obs工程中全工程验证通过后再整体批量从openeuler-risc-v向上游src-openeuler提交PR；

   因此，目前不同的软件包，对应的仓库分为两种：

   1. 默认：src-openeuler
   2. 构建失败的包：原始和最终的源码都是src-openeuler，但是在全obs工程未达成构建目标之前，修改的代码临时放openeuler-risc-v



   - 关于分支
     - 对应上述仓库管理关系，根据不同的分支工程，建立对应的源码分支，不同工程下的源码在其对应的分支上进行管理和提交、合入；（openeuler riscv下的master分支和22.03:LTS:Next分支都是来自于上游x86和arm的同版本工程；本身并无直接的关系）
     - 22.03-LTS-Next是22.03:LTS的一个预备版本，发版之前大家统一在这个工程上验证，有问题完成修改后将源码提交到对应的分支上，完成代码回合后才会生成正式的22.03-LTS版本。（这就存在部分源码包的版本还会变动）
     - 并不是每一个源码仓中的源码都有openEuler:22.03:LTS:Next分支的。
     - 目前的22.03的分支还未建立





## 2. [openEuler:Mainline:RISC-V](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V)

版本确定定位问题，是否进行持续维护？怎么维护？





## 3. 22.03LTS版本（openEuler:22.03:LTS:Next:RISC-V ）

### 3.1 现状

- 需求：从LTS版本主打长期维护+稳定性的考虑，22.03 oe-rv的功能以系统基础为主，在功能上初步讨论支持：

  - 内核

  - 容器：docker、isula

  - 语言包：java、python、go、ruby、perl、rust、scala...



- 计划：结合openeuler上游22.03LTS Release计划，oe-rv 22.03LTS计划：

  ![image-20211118091911807](C:/Users/cz/AppData/Roaming/Typora/draftsRecover/images/image-20211118091911807.png)

  | 发版需求                                        | 2021/11/1  | 2021/12/30 |
  | ----------------------------------------------- | ---------- | ---------- |
  | 开发                                            | 2021/11/1  | 2022/1/30  |
  | 代码回合（openeuler-risc-v向src-openeuler回合） | 2021/12/30 | 2022/1/30  |
  | 拉版本分支22.03 LTS                             |            | 2022/2/7   |
  | Alpha自验证                                     | 2022/2/7   | 2022/2/11  |



- 版本基线：（riscv原则上保持一致）

  | 软件包   | 当前版本 | 计划升级版本 | 升级完成时间 | [openEuler:Mainline:RISC-V](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V) | [openEuler:22.03:LTS:Next](https://build.openeuler.org/project/show/openEuler:22.03:LTS:Next) |
  | -------- | -------- | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | kernel   | 5.10     | 小版本升级   | 11.30        | 5.10                                                         |                                                              |
  | gcc      | 9.3      | 10.3         | 6.30         | 9.3.1                                                        | 10.3.1                                                       |
  | glibc    | 2.33     | 2.34         | 8.01         | 2.33                                                         | 2.34                                                         |
  | binutils | 2.34     | NA           | NA           | 2.34                                                         | 2.36.1                                                       |
  | libmpc   | 1.2.0    | 1.2.1        | 6.30         | 1.2.0                                                        | 1.2.0                                                        |
  | gmp      | 6.2.0    | 6.2.1        | 6.30         | 6.2.1                                                        | 6.2.1                                                        |



### 3.2 建设方案（todo）

#### 3.2.1 构建工程：

1. 建obs工程：

   从上游[openEuler:22.03:LTS:Next](https://build.openeuler.org/project/show/openEuler:22.03:LTS:Next) branch 出riscv的工程：openEuler:22.03:LTS:Next:RISC-V

   > x86和arrch的都是在[openEuler:22.03:LTS:Next](https://build.openeuler.org/project/show/openEuler:22.03:LTS:Next) 中由这一个工程管理的，riscv理想状态也需要在一个工程构建。
   >
   > 目前单独建工程是因为riscv这边的问题还比较多？

2. 建种子仓库：

   种子仓库：

   1. obs worker镜像中
   2. 种子仓库
      - 种子1：通过openeuler代码构建出来的rpm包：应该是自洽的
      - 用种子1进行滚动构建



   操作步骤：

   1. 在obs 任一工程中，branch openEuler:22.03:LTS:Next部分包源码，优先构建出glibc、gcc、libmpc、gmp、binutils 等一些基础包的rpm作为种子1

      > 由于22.03的代码版本实际上和21.09非常接近（或者一样，没有严格去对比）。因此本工作其实孙喆炘已经在其baseOS工作中完成：
      >
      > - stage1:23个包全部构建成功
      >   - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
      > - Stage2: 82个包 68个成功
      >   - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2
      > - Stage3: 139个包 104个成功
      >   - https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:21.09:stage3
      >
      >
      >
      > 不放心版本差异的，这里也有之前临时验证有的基于openEuler:22.03:LTS:Next branch出的部分包可做种子：
      >
      > - https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1

   2. 然后创建种子管理工程：openEuler:22.03:LTS:Next:RISC-V:selfbuild:BaseOS工程， 将种子1通过其管理起来；

   3. 将种子1配置为openEuler:22.03:LTS:Next:RISC-V 工程的依赖仓，让工程自己滚动构建？

      > 这里怎么启动自动构建？

   说明：整个过程中，原则上软件包（版本）不应该变化；这样才能实现滚动构建。一旦整个系统中部分软件包版本变化，就可能导致自构建混乱？

   > 这个问题，其实是有阶段性的，据孙喆炘反馈，在x86、arm64之前的版本中，也是没有实现自举构建的。但是在22.03版本中，则开始尝试达成这一目标。——》所以我怀疑我们22.03要做的莫非不是验证哪些能够构建成功，并切割出一个能够构建成功的软件包的子集合出来？（随便脑洞一下）



#### 3.2.2 种子仓库：

- 通过obs工程进行管理：

  > 参考上游和其它release版，依赖仓也是通过obs工程管理，名字一般含有selfbuild字眼；

- 可以尝试按照openEuler:Mainline:RISC-V现行的将依赖仓进行分组管理：
  - 语言包相关分组
  - 非语言包相关的基础系统包分一组
  - 编译器相关分一组
  - ……

  具体参考openEuler:Mainline:RISC-V当前依赖仓实例openEuler:selfbuild:function：https://build.openeuler.org/repositories/openEuler:selfbuild:function。已经逐步按照语言包将依赖包进行分别管理：python、ruby。

  - 只要源码是一直的，依赖仓的分组中的包，允许存在重复的情况（一个包同时存在不同的组中）



#### 3.2.3 源码仓：

1. 为openeuler-risc-v源码仓的源码建立openEuler:22.03:LTS:Next 分支；

2. master工程的修复，源码修改提交到master；针对22.03:LTS:Next所做的源码修改，源码提交到22.03:LTS:Next分支；



### 3.4 计划

一周内：

1. obs工程建立
2. 种子仓库
3. 生成种子1

两周内：

1. 基于种子1,openEuler:22.03:LTS:Next:RISC-V 4167个包构建状态验证；——》这样才能了解现状，知道哪些包有问题需要修复

2. 基于结果，从以下两个角度分析包构建情况，整理修复优先级：

   （1）依赖关系底层的包

   （2）对比minios的450+个包

3. 开始针对构建失败的包修复
