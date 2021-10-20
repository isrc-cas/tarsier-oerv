# 工作总结 [9.23-10.20]

## 过去两周的进展

中间经历了一个十一长假，跳过一次双周例会。



2. [WIP] openEuler:Mainline:RISC-V工程构建：

| datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
| -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
| 20210908 | 1907      | 252    | 1889         | 16     | 1        | 62       |
| 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
| 20210926 | **2206**  | 266    | 1576         | 16     | 1        | 62       |
| 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
| 20211009 | 2312      | 168    | 1569         | 16     | 1        | 61       |
| 20211020 | **2321**  | 166    | 1562         | 16     | 1        | 61       |

- 新增succeeded包：15个
- LLVM工具链构建成功



2、系统可视化桌面功能支持

（1）xfce

（2）lxde：梳理了所需的包、安装后渲染存在问题，放弃；

- https://build.openeuler.org/project/show/home:pandora:lxde



3、[进行中]BaseOS for openEuler RISC-V  @孙喆炘

- stage1:23个包全部构建成功：https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
- Stage2: 82个包 68个成功：https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2




## 未来两周计划

1. 继续mainline上failed和  unresolvable包的fix；

   目标：数量上力争10月底能够超过2500

   内容：从xfce自上而下梳理所必须的包，对mainline进行查缺补漏

2. 对xfce在D1上进行安装测试和包的查缺补漏

   配置源：https://build.openeuler.org/project/show/home:pandora:xfce 和https://build.openeuler.org/project/show/home:pandora:xfce4 进行安装，对xfce安装所缺少的包进行梳理和排查。

