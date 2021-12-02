# openEuler for RISCV

## 维护中的分支

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



## [openEuler:Mainline:RISC-V](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V)

版本确定定位问题，是否进行持续维护？怎么维护？





## openEuler:22.03:LTS:Next:RISC-V 

- 需求：从LTS版本主打长期维护+稳定性的考虑，22.03 oe-rv的功能以系统基础为主，在功能上初步讨论支持：

  - 内核

  - 容器：docker、isula

  - 语言包：java、python、

    

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



### 建设方案

#### 构建工程：

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



#### 种子仓库：

- 通过obs工程进行管理：

  > 参考上游和其它release版，依赖仓也是通过obs工程管理，名字一般含有selfbuild字眼；

- 可以尝试按照openEuler:Mainline:RISC-V现行的将依赖仓进行分组管理：
  - 语言包相关分组
  - 非语言包相关的基础系统包分一组
  - 编译器相关分一组
  - ……

  具体参考openEuler:Mainline:RISC-V当前依赖仓实例openEuler:selfbuild:function：https://build.openeuler.org/repositories/openEuler:selfbuild:function。已经逐步按照语言包将依赖包进行分别管理：python、ruby。

  - 只要源码是一直的，依赖仓的分组中的包，允许存在重复的情况（一个包同时存在不同的组中）



#### 源码仓：

1. 为openeuler-risc-v源码仓的源码建立openEuler:22.03:LTS:Next 分支；

2. master工程的修复，源码修改提交到master；针对22.03:LTS:Next所做的源码修改，源码提交到22.03:LTS:Next分支；

   

