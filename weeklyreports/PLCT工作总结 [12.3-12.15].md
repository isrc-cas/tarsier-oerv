# 工作总结 [12.3-12.15]

## 过去两周的进展

1. 22.03:LTS开展：

   - MiniOS 软件包范围（450+个包）： https://github.com/plctlab/openEuler-riscv/issues/187
   
   - **[新]** 种子仓库stage1：https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1
   
     - glibc从未成功过
   
   - **[新]** openEuler:22.03:LTS:Next for RISC-V（4167个包）：https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next

     - 成功185个
     - glibc从未成功
   
   - 新PR：提交到22.03分支
   
     - [subunit](https://gitee.com/openeuler-risc-v/subunit/pulls/1)
   
     - [qt](https://gitee.com/openeuler-risc-v/qt/pulls/1)
   
       >提交流程：
       >
       >第一种情况：对于从未fork到openeuler-risc-v源码仓的包，现在fork后，源码仓中有新增的22.03:LTS:Next分支，因此直接按需提交：
       >
       >- 针对mainline的fix，提交到openEuler-RISC-V:master
       >- 针对22.03的fix，提交到openEuler-RISC-V:openEuler-22.03-LTS-Next
       >
       >第二种情况：对于在上游22.03:LTS:Next分支创建之前就fork到openeuler-risc-v源码仓的包，riscv源码仓中无openEuler-22.03-LTS-Next的：
       >
       >- 针对mainline的fix，提交到openEuler-RISC-V:master
       >- 针对22.03的fix，**新建一个与上游同名的分支：openEuler-RISC-V:openEuler-22.03-LTS-Next**。提交到该分支。后续再完成openeuler-risc-v向上游src-openeuler的回合。
   
       
   
2. openEuler:Mainline:RISC-V 包修复

   | datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
   | -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
   | 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
   | 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
   | 20211030 | 2323      | 164    | 1562         | 16     | 1        | 61       |
   | 20211130 | 2441      | 146    | 1475         | 2      | 1        | 61       |
   | 20211215 | 2512      | 162    | 1390         | 2      | 1        | 60       |

   - 新增成功：71个

     perl相关包基本上都构建成功。

     | 包名                              | 1215构建状态 | 之前构建状态 |
     | --------------------------------- | ------------ | ------------ |
     | SDL2                              | succeeded    | unresolvable |
     | cloc                              | succeeded    | unresolvable |
     | digest-list-tools                 | succeeded    | unresolvable |
     | erlang                            | succeeded    | unresolvable |
     | fluidsynth                        | succeeded    | unresolvable |
     | gdm                               | succeeded    | unresolvable |
     | glusterfs                         | succeeded    | unresolvable |
     | gnome-control-center              | succeeded    | unresolvable |
     | gnome-settings-daemon             | succeeded    | unresolvable |
     | kiwi                              | succeeded    | unresolvable |
     | libfabric                         | succeeded    | unresolvable |
     | libiscsi                          | succeeded    | unresolvable |
     | linuxconsoletools                 | succeeded    | unresolvable |
     | opensm                            | succeeded    | unresolvable |
     | orca                              | succeeded    | unresolvable |
     | ostree                            | succeeded    | unresolvable |
     | perl-Alien-Build                  | succeeded    | unresolvable |
     | perl-Alien-Libxml2                | succeeded    | unresolvable |
     | perl-Archive-Zip                  | succeeded    | unresolvable |
     | perl-B-Lint                       | succeeded    | unresolvable |
     | perl-BibTeX-Parser                | succeeded    | unresolvable |
     | perl-Config-General               | succeeded    | unresolvable |
     | perl-Expect                       | succeeded    | unresolvable |
     | perl-FFI-CheckLib                 | succeeded    | unresolvable |
     | perl-File-MimeInfo                | succeeded    | unresolvable |
     | perl-IO-All                       | succeeded    | unresolvable |
     | perl-IPC-Run                      | succeeded    | unresolvable |
     | perl-JSON-XS                      | succeeded    | unresolvable |
     | perl-MIME-Lite                    | succeeded    | unresolvable |
     | perl-MIME-Types                   | succeeded    | unresolvable |
     | perl-Mail-IMAPTalk                | succeeded    | unresolvable |
     | perl-Module-Install-AutoLicense   | succeeded    | unresolvable |
     | perl-Module-Install-ReadmeFromPod | succeeded    | unresolvable |
     | perl-Module-Install-Repository    | succeeded    | unresolvable |
     | perl-Module-Package               | succeeded    | unresolvable |
     | perl-Module-Package-Au            | succeeded    | unresolvable |
     | perl-Net-Server                   | succeeded    | unresolvable |
     | perl-SUPER                        | succeeded    | unresolvable |
     | perl-Term-Table                   | succeeded    | unresolvable |
     | perl-Test-MockModule              | succeeded    | unresolvable |
     | perl-Test-Simple                  | succeeded    | unresolvable |
     | perl-Test2-Suite                  | succeeded    | unresolvable |
     | perl-Unicode-EastAsianWidth       | succeeded    | unresolvable |
     | perl-Unicode-LineBreak            | succeeded    | unresolvable |
     | perl-XML-LibXML                   | succeeded    | unresolvable |
     | perl-XML-Simple                   | succeeded    | unresolvable |
     | pipewire                          | succeeded    | unresolvable |
     | portaudio                         | succeeded    | unresolvable |
     | python-behave                     | succeeded    | unresolvable |
     | qperf                             | succeeded    | unresolvable |
     | speech-dispatcher                 | succeeded    | unresolvable |
     | tslib                             | succeeded    | unresolvable |
     | wxGTK3                            | succeeded    | unresolvable |
     | xdp-tools                         | succeeded    | unresolvable |
     | attest-tools                      | failed       | unresolvable |
     | clevis                            | failed       | unresolvable |
     | grub2                             | failed       | unresolvable |
     | libvma                            | failed       | unresolvable |
     | mstflint                          | failed       | unresolvable |
     | mvapich2                          | failed       | unresolvable |
     | papi                              | failed       | unresolvable |
     | perftest                          | failed       | unresolvable |
     | scap-workbench                    | failed       | unresolvable |

   - 新提交的PR：

     - [mariadb](https://gitee.com/openeuler-risc-v/mariadb/pulls/1)
     - [gsl](https://gitee.com/openeuler-risc-v/gsl/pulls/1)
     - [augeas](https://gitee.com/openeuler-risc-v/augeas/pulls/1)

3. BaseOS for openEuler：用作基础种子

   - 【停止的】stage1:23个包全部构建成功
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
   - 【停止的】Stage2: 82个包（10个从未成功）
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2
   - Stage3：139个包（19个从未成功）
     - https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:21.09:stage3

   

## 计划

1. 为22.03创建一个种子仓库

   - 之前是引用已有的工程构建仓库、或者之前建立的种子文件夹

     问题：

     （1）构建速度慢、结果远低于预期

     > 原因是开了Use for Build Flag自构建，因此每新生成一个rpm就会引发工程重新构建；

     （2）基础包glibc未成功：因为很多包都依赖glibc，我个人有个想法就是优先让22.03工程中构建成功的gcc、glibc的rpm去继续后续的全工程构建。

     ——》现在根据版本，将22.03的构建成功的rpm下载，做成新的种子文件夹

2. 修包

   - 重要的包修不动
   - 不重要的包修复后不会对整个工程产生根本上的改变



## 问题沟通

\1. 原计划的obs worker接入华为云obs server由于网络问题，暂时未接入成功。因此设想在PLCT搭建一个obs server，所有的源码和obs配置可否在gitee仓库进行统一管理（达到一致）

处理：

（1）将openeuler riscv相关的工程配置、包配置等更新到最新，将gittee url地址给出 @张旭舟

（2）搭建PLCT obs 环境副本，扩展obs构建资源；  @吴伟



2.基础语言包的升级

比如：perl包从5.28升级到5.32版本；但是目前整个构建平台都没有5.32的perl的rpm包，怎么处理？

举例：openeuler升级python，从python3.8升级为python3.10的过程是如下的：

（1）将源码升级为python3.10，在spec中将旧版本的so库拷贝进来，生成一个Python中间版本（pythonM），这样pythonM就既提供了3.8的运行库，又提供了3.10的开发库；

（2）将pythonM放到种子仓库中，这样依赖python3.8的包还能继续运行，新构建的包都会依赖3.10。当所有的包都能够支持3.10后，就将种子仓库的oythonM去掉，python rpm更新到3.10；

备注：如果spec 版本信息是高版本，但是spec中又有低版本描述信息——》这种情况说明是中间版本，对照上述步骤进行处理。



\3. 工程维护方式：自举工程有问题，将精力集中的mainline:riscv；

目前mainline:riscv一直在维护和更新：

不刻意维持22.03版本对齐，主要以解决问题为主，但是修包之前会将代码更新到master最新版本；

mainline:riscv作为riscv的master，一直跟随上游mainline滚动更新。



\4. 目前22.03:LTS:RISC-V个人验证工程（https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next）的构建效率非常慢，不能了解22.03整体问题。

原因：该工程开启了Use for Build Flag，这样工程每新生成一个rpm包，就会自动更新依赖仓（导致工程matechage），从而启动一轮新的构建。——》这是最终要达到的目的和理想的做法，这样效率很低

建议可以尝试这样做：再启动一个个人工程，用不同的方式去构建：

​      工程不开启Use for Build Flag，用手动管理种子文件夹的方式去批量更新：

​      可以用以下依赖仓去构建工程：

​      （1）mainline:riscv的工程仓库

​      （2）https://build.openeuler.org/project/show/home:pandora:BaseOS 工程仓库

- 这样构建成功的rpm，手动下载后创建新的种子文件夹作为依赖仓（去掉之前上述配置的2个工程依赖），重新构建。——》用手动批量管理rpm启动循环构建的方式去替代obs自身的单rpm更新循环构建，以提高效率。

@席静



\5. 22.03公开工程是否还需要创建？

目前已经在个人账户下创建了22.03的验证项目，是否还需要创建公开工程？公开工程在操作方面会受限，不灵活；

个人工程构建资源有限，高峰时候存在大量构建任务排队的情况（公开工程和个人工程构建资源是分开的）

申请新的构建资源提供给个人工程使用 @张旭舟



\6. 对内核进行了配置的更新，将配置同步到gitee仓库

内核kcapi选项没有打开，导致编译不过；已经针对该问题修改了内核配置——》将配置修改更新到gitee仓库，并在后续保持信息及时同步。 @王俊强



