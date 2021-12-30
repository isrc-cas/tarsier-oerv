# 工作总结 [12.16-12.29]

## 过去两周的进展

1. 22.03:LTS开展：

   - MiniOS 软件包范围（450+个包）： https://github.com/plctlab/openEuler-riscv/issues/187

   - 种子仓库stage1：https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1

     - systemd、glibc等包从未成功过，对这些包进行问题分析和fix
       - systemd：已经修复：https://build.openeuler.org/package/show/home:xijing:22.03:LTS:Next:stage1:failedfix/systemd
       - glibc：进行中

   - openEuler:22.03:LTS:Next for RISC-V（4167个包，**开Use for Build Flag**）：https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next

     > 工程打开了Use for Build Flag，当工程repo更新后会自动重新构建，【自举构建】模式进行构建。——》进度缓慢

     - 成功185个

   - **[新]** openEuler:22.03:LTS:Next for RISC-V（4167个包，未开Use for Build Flag）：https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next

     > 仿照openEuler:Mainline:RISC-V，主要在代码版本升级的情况下，基于openEuler:Mainline:RISC-V的工程repo和一些base 工程repo，对所有的包进行构建状态摸底。目前还未完整的构建一轮。

      [succeeded: 1110](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&defaults=0&repo_riscv64_stage1=1&succeeded=1)

      [failed: 382](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&defaults=0&failed=1&repo_riscv64_stage1=1)

      [unresolvable: 1497](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&defaults=0&repo_riscv64_stage1=1&unresolvable=1)

      [broken: 2](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&broken=1&defaults=0&repo_riscv64_stage1=1)

      [blocked: 625](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&blocked=1&defaults=0&repo_riscv64_stage1=1)

      [scheduled: 494](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&defaults=0&repo_riscv64_stage1=1&scheduled=1)

      [building: 5](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&building=1&defaults=0&repo_riscv64_stage1=1)

      [excluded: 59](https://build.openeuler.org/project/monitor/home:xijing:branches:openEuler:22.03:LTS:Next?arch_riscv64=1&defaults=0&excluded=1&repo_riscv64_stage1=1)

   - 新PR：提交到22.03分支

     - [jimtcl](https://gitee.com/openeuler-risc-v/jimtcl/pulls/1)

     - [openssl](https://gitee.com/openeuler-risc-v/openssl/pulls/1)

     - [ systemd](https://gitee.com/openeuler-risc-v/systemd/pulls/1)

     - [mstflint](https://gitee.com/openeuler-risc-v/mstflint/pulls/1)

     - [ rdma-core](https://gitee.com/openeuler-risc-v/rdma-core/pulls/1)

     - [etmem](https://gitee.com/openeuler-risc-v/etmem/pulls/1)

       

2. openEuler:Mainline:RISC-V 包修复

   | datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
   | -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
   | 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
   | 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
   | 20211030 | 2323      | 164    | 1562         | 16     | 1        | 61       |
   | 20211130 | 2441      | 146    | 1475         | 2      | 1        | 61       |
   | 20211215 | 2512      | 162    | 1390         | 2      | 1        | 60       |
   | 20211229 | 2522      | 154    | 1389         | 1      | 1        | 60       |

   - 新提交的PR：

     - [ sscg](https://gitee.com/openeuler-risc-v/sscg/pulls/2)
     - [mariadb](https://gitee.com/openeuler-risc-v/mariadb/pulls/3)
     - [libkcapi](https://gitee.com/openeuler-risc-v/libkcapi/pulls/2)
   - 正在进行的：
     - 

   

3. PLCT搭建了obs server： https://build.tarsier-ci.org/

   具体情况？是否能够帮助提高构建效率？

   

4. 主要工程汇总（可选择性的用作工程依赖仓）：

   | 工程                             | 工程链接                                                     | 可用仓库                                                     | 说明                                   |
   | -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------- |
   | riscv主工程(mater)               | https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V | [standard_riscv64](https://build.openeuler.org/project/repository_state/openEuler:Mainline:RISC-V/standard_riscv64) | 主工程                                 |
   | 22.03LTSNext-验证1：zxsun        | https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:22.03:next | [stage1_1a](https://build.openeuler.org/project/repository_state/home:zxs-un:openEuler:riscv64:22.03:next/stage1_1a) | 自举构建-尝试                          |
   | 22.03LTSNext-验证2：xijing       | https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next | [riscv64_stage1](https://build.openeuler.org/project/repository_state/home:xijing:branches:openEuler:22.03:LTS:Next/riscv64_stage1) | 主要用于2203总体构建状态摸底           |
   | python                           | https://build.openeuler.org/project/show/home:lvxiaoqian:python3.8 | standard_riscv64                                             |                                        |
   | 俊强                             | https://build.openeuler.org/user/show/pandora                |                                                              | 包含各种工程，可选对应工程作为构建种子 |
   |                                  |                                                              |                                                              |                                        |
   | BaseOS(可用于2203构建种子的工程) | https://build.openeuler.org/project/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1 | stage1_2                                                     | 对齐22.03版本                          |
   |                                  | https://build.openeuler.org/project/show/home:pandora:BaseOS | standard_riscv64                                             | 对齐22.03版本                          |
   |                                  | https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:BaseOS:stage1 | [stage2_5](https://build.openeuler.org/project/repository_state/home:zxs-un:openEuler:riscv64:BaseOS:stage1/stage2_5) | 对齐21.09版本                          |
   |                                  | https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:BaseOS:stage2 | [stage2_10a](https://build.openeuler.org/project/repository_state/home:zxs-un:openEuler:riscv64:BaseOS:stage2/stage2_10a) | 对齐21.09版本                          |
   |                                  | https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:21.09:stage3 | stage3_1  根据构建状态自行选择1个或者多个                    | 对齐21.09版本                          |







## 现状总结

1. 22.03摸底工程：
   - 构建速度未达到预期。目前估计还需要一周才能完成一遍构建。
   - 22.03构建效果对照mainline:RISC-V也不是很可观。还有1000多个未构建完的情况下，构建失败数量当前已经接近400个；
2. 语言包升级：目前的重点和难点，已经在开展中：
   - Java
   - python
   - perl
   - golang：引擎成功，部分依赖未成功
   - nodejs：编译成功，打包失败
   - php
   - rust
   - ruby
   - ocaml
   - erlang
3. 门禁：未开始
4. 镜像工具：是否还需要做什么？



## 计划

目前的工作重心有两大块：

1. 语言包的升级

   在mainline:RISC-V工程上，对Java、python、perl、golang、nodejs、php、rust、ruby、ocaml、erlang等进行版本升级、构建修复等。

2. 按照个人仓库中的22.03构建的情况，对基础性的包&从未构建成功的包进行修复。

   - [完成]systemd

   - [glibc](https://build.openeuler.org/package/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1/glibc)

   - [coreutils](https://build.openeuler.org/package/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1/coreutils)

   - [bison](https://build.openeuler.org/package/show/home:xijing:branches:openEuler:22.03:LTS:Next:stage1/bison)

     参考21.09，以下包是大概率构建失败的包（目前在22.03中block或者unresolvable）：

     [boost](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/boost)

     [chrony](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/chrony)

     [clang](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/clang)

     [e2fsprogs](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/e2fsprogs)

     [gettext](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/gettext)

     [golang](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/golang)

     [iptables](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/iptables)

     [keyutils](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/keyutils)

     [libdb](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/libdb)

     [libdnf](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/libdnf)

     [libmodulemd](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/libmodulemd)

     [libtool](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/libtool)

     [llvm](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/llvm)

     [openjdk-11](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/openjdk-11)

     [openssl](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/openssl)

     [perl](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/perl)

     [python3](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/python3)

     [subversion](https://build.openeuler.org/package/show/home:zxs-un:openEuler:riscv64:21.09:stage3/subversion)

3. 针对mainline:RISC-V工程构建失败的包进行修复（属于能做什么做什么）

   

