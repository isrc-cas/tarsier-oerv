## openEuler for RISC-V

1. openEuler:Mainline:RISC-V 包修复

   | datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
   | -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
   | 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
   | 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
   | 20211030 | 2323      | 164    | 1562         | 16     | 1        | 61       |

   - 新增成功：14个
     - LLVM工具链构建成功：[PR](https://gitee.com/openeuler-risc-v/llvm/pulls/2)   [构建日志](https://build.openeuler.org/package/live_build_log/openEuler:Mainline:RISC-V/llvm/standard_riscv64/riscv64)
     - 包状态变更详情：[link](https://github.com/plctlab/openEuler-riscv/blob/main/data/compare/obsBuild-20211020-1435-compare.xlsx)
   - 进行中的包：
     - python3.9：[issue#134](https://github.com/plctlab/openEuler-riscv/issues/134)
     - bazel：[issue#166](https://github.com/plctlab/openEuler-riscv/issues/166)  [obslink](https://build.openeuler.org/package/show/home:mc:branches:openEuler:Mainline:RISC-V/bazel)
     - openmpi：[issue#150](https://github.com/plctlab/openEuler-riscv/issues/150)  [obslink](https://build.openeuler.org/package/show/home:mc:branches:openEuler:Mainline:RISC-V/openmpi)
     - [【构建失败】原因分析包括：yum-metadata-parser、rubygem-redcarpet、rubygem-bindex、squid、rubygem-unf_ext、scap-security-guide、rubygem-sqlite3](https://github.com/plctlab/openEuler-riscv/issues/168)
     - 

2. 系统可视化桌面功能支持Xfce：

   - D1上可用，继续完善和提升用户体验
     - https://build.openeuler.org/project/show/home:pandora:xfce
     - https://build.openeuler.org/project/show/home:pandora:xfce4
     - xfce测试：https://github.com/plctlab/openEuler-riscv/issues/181
   - Lxde：梳理了所需的包、安装后渲染存在问题，优先级调低；
     - https://build.openeuler.org/project/show/home:pandora:lxde
     - lxde测试：https://github.com/plctlab/openEuler-riscv/issues/167

3. BaseOS for openEuler

   - stage1:23个包全部构建成功
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
   - Stage2: 82个包 68个成功
     - https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2
   - 关注的包：
     - automake 可复现成功但不稳定
     - util-linux 可复现成功但不稳定
     - coreutils 发现它的变更对其余包的测试用例影响较大

4. 文档：

   - [osc本地构建](https://github.com/plctlab/openEuler-riscv/issues/83)
   - [workflow-for-build-a-package](https://github.com/plctlab/openEuler-riscv/blob/main/quicklystartbuild/workflow-for-build-a-package.md)
   - [obs-help](https://github.com/plctlab/openEuler-riscv/blob/main/quicklystartbuild/obs-help.md)
   - [lxde-test](https://github.com/xijing21/rvOe_study/blob/main/D1/desktop-lxde/lxde-test.md)





# 成员交付成果清单

请大家参考如下信息要素提交可见交付成果：（没有的可不列出）

构建包任务类：

- XXXX包：
  - issue：
  - obs：
  - PR：
  - 文档：

其它任务：

- issue标题：
  - issue链接：
  - PR：
  - 文档：

笔记类（这里特指自己学习、工作中总结的文档，不是以issue方式指定的任务）：

- 文档标题、链接

问题类（工作中发现和遇到的问题，必须以公开的方式可见才行，非可见不算可见交付）

- issue标题和链接



### 马驰

构建包任务类：

- bazel包：
  - issue：https://github.com/plctlab/openEuler-riscv/issues/166
  - obs：https://build.openeuler.org/package/show/home:mc:branches:openEuler:Mainline:RISC-V/bazel
  - PR：
  - 文档：
  
- openmpi包：
  - issue：https://github.com/plctlab/openEuler-riscv/issues/150
  - obs：https://build.openeuler.org/package/show/home:mc:branches:openEuler:Mainline:RISC-V/openmpi
  - PR：
  - 文档：

其它任务：

- issue标题：完成osc本地构建的文档
  - issue链接：https://github.com/plctlab/openEuler-riscv/issues/83
  - PR：
  - 文档：




### 孙喆炘

详见：https://github.com/plctlab/openEuler-riscv/issues/178



### 刘佳伟

详见：https://github.com/plctlab/openEuler-riscv/issues/178



### 李诗洋




### 孙浩翔





### 许志凌





### 邹通成





### 许嘉玲





### 颛孙宇翔 



### 高世豪





### 袁政





### 刘洋





### 温智翔



### 杨心仪



### 陈泽睿



### 冯宇

