# 工作总结 [11.18-12.2]

## 过去两周的进展

1. openEuler:Mainline:RISC-V 包修复

   | datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
   | -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
   | 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
   | 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
   | 20211030 | 2323      | 164    | 1562         | 16     | 1        | 61       |
   | 20211130 | 2441      | 146    | 1475         | 2      | 1        | 61       |

   - 新增成功：118个
   - 新提交的PR：
     - [openblas](https://gitee.com/openeuler-risc-v/openblas/pulls/1)
     - [apr](https://gitee.com/openeuler-risc-v/apr/pulls/1)
     - [haproxy](https://gitee.com/openeuler-risc-v/haproxy/pulls/1)
     - [kexec-tools](https://gitee.com/openeuler-risc-v/kexec-tools/pulls/1)
     - [containerd](https://gitee.com/openeuler-risc-v/containerd/pulls/1)
     - [runc](https://gitee.com/openeuler-risc-v/runc/pulls/1)
     - [gd](https://gitee.com/openeuler-risc-v/gd/pulls/1)
     - [python3](https://gitee.com/openeuler-risc-v/python3/pulls/1)

2. BaseOS for openEuler：用作基础种子

   - stage1:23个包全部构建成功
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
   - Stage2: 82个包（11个从未成功）
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2
   - Stage3：139个包（20个从未成功）
     - https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:21.09:stage3

3. 22.03:LTS发版相关

   - 需求：从LTS版本主打长期维护+稳定性的考虑，22.03 oe-rv的功能以系统基础为主，在功能上初步讨论支持：
     - 内核
     - 容器：docker、isula
     - 语言包
     
   - 计划：结合openeuler上游Release SIG计划和版本基线要求：

     - 结合openeuler上游22.03LTS Release计划，oe-rv 22.03LTS计划：

     | 发版需求                                        | 2021/11/1  | 2021/12/30 |
     | ----------------------------------------------- | ---------- | ---------- |
     | 开发                                            | 2021/11/1  | 2022/1/30  |
     | 以功能支持+fix问题包的主要开发阶段(测试驱动)    | 2021/11/1  | 2021/12/30 |
     | 以测试为主的完善阶段                            | 2021/12/30 | 2022/1/30  |
     | 代码回合（openeuler-risc-v向src-openeuler回合） | 2021/12/30 | 2022/1/30  |
     | Alpha自验证                                     | 2022/2/7   | 2022/2/11  |

     - openeuler上游22.03LTS 版本基线：（riscv原则上保持一致）

       | 软件包   | 当前版本 | 计划升级版本 | 升级完成时间 | [openEuler:Mainline:RISC-V](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V) | [openEuler:22.03:LTS:Next](https://build.openeuler.org/project/show/openEuler:22.03:LTS:Next) |
       | -------- | -------- | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
       | kernel   | 5.10     | 小版本升级   | 11.30        | 5.10                                                         |                                                              |
       | gcc      | 9.3      | 10.3         | 6.30         | 9.3.1                                                        | 10.3.1                                                       |
       | glibc    | 2.33     | 2.34         | 8.01         | 2.33                                                         | 2.34                                                         |
       | binutils | 2.34     | NA           | NA           | 2.34                                                         | 2.36.1                                                       |
       | libmpc   | 1.2.0    | 1.2.1        | 6.30         | 1.2.0                                                        | 1.2.0                                                        |
       | gmp      | 6.2.0    | 6.2.1        | 6.30         | 6.2.1                                                        | 6.2.1                                                        |

   - 开展：
     
     - MiniOS 软件包范围（450+个包）： https://github.com/plctlab/openEuler-riscv/issues/187
     
     - **[新]** 种子仓库stage1：https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1
     - **[新]** openEuler:22.03:LTS:Next for RISC-V（4167个包）：https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next
     
   - 基础设施：
     - 完成PLCT2台obs worker搭建，正在接入华为云obs server
     - 新建仓库（打包构建所需用到的各类工具）：https://github.com/plctlab/openeuler-riscv-devtools
     
     

4. 新功能支持：

   - Docker功能已经能够支持（rpm安装）
     - docker包工程：https://build.openeuler.org/project/show/home:pandora:docker
     - 基于oe源yum安装已经能够成功安装和运行：https://github.com/plctlab/openEuler-riscv/issues/194







---

### 22.03:LTS构建方案

新建22.03工程openEuler:riscv64:22.03:next（ branch 22.03:LTS:Next  4167个包），开始构建:https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next

- 种子仓库：

  - 自己做的一个原始的种子仓库（假设叫baseSeed吧）:https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1

    > 这个是孙喆炘BaseOS 在22.03上的同类工程，当软件包源码版本一致时，可以直接使用孙喆炘之前构建好的stage3（stage2/stage1）中最全+最新的构建repo；

  - 构建openEuler:riscv64:22.03:next    Seed：baseSeed

    - 构建成功成果——》selfSeed1

      > 这里肯定只有部分成功，每次构建都只有部分包会成功；但是首先需要让glibc、gcc、libmpc、gmp、binutils这些包成功；

  - 再次构建openEuler:riscv64:22.03:next     Seed：**selfSeed1**+baseSeed

    - 构建成功成果——》selfSeed2

  - 再次构建openEuler:riscv64:22.03:next     Seed：**selfSeed2**+selfSeed1+baseSeed

    后面依次类推，但是肯定会出现需要新的依赖包：用openEuler:Mainline:RISC-V工程构建的rpm（mainlineRiscvSeed）去完善依赖仓，推动构建。



问题：

1、 是否对openEuler:riscv64:22.03:next 的4167个包进行分组？并对不同的分组放在不同的subproject中管理？

分组目前肯定不可能一步达到理想状态，只是探索式推进一些（会存在也允许存在分组不合理）

为什么会提出分组？

分组的目的？

分组的原则？

分组的好处？



### PR问题讨论

1. pr提交不规范

   - 要求把问题、自己对问题的分析、修改的思路、修改后的验证结论等写出来，让maintainer能够了解整个修改的过程；（这个过程可以是在pr中简单描述，也可以贴自己分析issue链接）

     > pr其实是一种交流方式，下游和上游的沟通桥梁
     >
     > 每个maintainer不是神，是人，需要贡献者去把问题说清楚，否则也很难合并

2. 离职实习生未跟踪完成的pr

   - [sscg](https://gitee.com/openeuler-risc-v/sscg/pulls)——》超时问题

     

3. 当前未合并的pr，在解决问题方面，有哪些问题、不规范的做法？

   - 提交的代码版本，需要是构建工程中对应的版本

     - [python3](https://gitee.com/openeuler-risc-v/python3/pulls/1)

       > 源码仓中无3.9版本，无法提交PR，关闭pr

   - spec & 源码包 

     - [containerd](https://gitee.com/openeuler-risc-v/containerd/pulls/1)
     - [runc](https://gitee.com/openeuler-risc-v/runc/pulls/1)

     

### 消息同步

Open Board Task Force会议：
汤亮和Yang 提到了生态也要软件共建；然后关于软件部分提到了如下：

1. 软件社区的建立：有人提了一嘴开源芯片研究院去跟；刘寿永老师说到时候会邀请软件所参加；
2. 考虑在软件层面去支持不同的开发板：软件参考平台
3. openEuler和OpenHarmony两个系统到底选哪个——》有人说openeuler目前成熟些
4. 被问openeuler情况，同时也询问了各开发板的应用场景、对系统的需求——》刘寿永老师就说下次专门组会议讨论下



