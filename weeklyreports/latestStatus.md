docker 运行 riscv qemu :

 riscv qemu 里面跑的 riscv docker :

在Qemu RISCV64虚拟机中安装Docker并运行RISCV Linux:https://zhuanlan.zhihu.com/p/399366057 





 oE/D1 上 docker 

https://github.com/plctlab/openEuler-riscv/issues/25
@吴伟 看看评论倒数第二条，目前是卡在这里，any idea？

之前的问题可能是后台有多个containerd在运行导致的，我后来手动kill掉，就好使了

 



这周日之前，我把 tarsier-ci OBS 和 code 配置好

之前已经和杨昕商量过了，bootstrap工程本身没有以openeuler官方的账户建立在obs上，现在只有和forPLCT文件夹同步的计划，再增加新的种子文件夹就越变越多，所以我现在寄希望于PLCT自己的obs



不需要再用脚本整理这75个包的依赖关系，它们是一个Linux发行版中基础的基础

采用脚本解析spec文件的方式给出依赖图，并不适用于bootstrap阶段的基础包，对这类基础包的依赖往往会在spec中直接省略

计划是参考 https://github.com/zxs-un/fedora-riscv-bootstrap 



oE riscv 2109拉出来之后就和master分叉了，2203从master拉出来。现在的main工程是大概2个月前从master 取的，那个时候还没走有2109，后面解决构建问题过程里边有一些包也升到了master的最新

目前x86/aarch64的main上，kernel 5.10   glibc 2.34  gcc 10.3.1

当前oe riscv 的kernel 5.10   glibc 2.33  gcc 9.3.1

xz：像glibc的master  上游8月1号发了2.34，oe的glibc master升到了2.34，然后好多包都编不过了

我是说 一般即使是滚动更新也不会在主线直接跟glibc。那会导致很多软件不通过的。如果要追也是开一个实验性分支来做

oE还不是“大发行版”。几大发行版有没有跟到glibc2.34的？ 我本能的觉得这个策略或决策… hmm，是不打算有客人啊

那么“发行版里的软件包具体版本怎么定就是版本经理和包maintainer定了” 如果包含了glibc，实际上就新分出来了

wjm：22.03 之前这 6 个月 glibc 2.34 这块会是一个比较大的风险点，但没有回头路了。

这要看 glibc 的前向兼容情况了，按我经验一般还好。

之前 openEuler 20.03 LTS 版本太老才容易出这类问题，因为这些二进制包都依赖更新的 glibc 。

那要看 rpm 包做的情况了，glibc 相关的依赖一般即使是 2.34 ，也会把 2.33 以及更早的也都提供出来。

给你看一下 20.03 上的提供：

libc.so.6()(64bit)
libc.so.6(GLIBC_2.17)(64bit)
libc.so.6(GLIBC_2.18)(64bit)
libc.so.6(GLIBC_2.22)(64bit)
libc.so.6(GLIBC_2.23)(64bit)
libc.so.6(GLIBC_2.24)(64bit)
libc.so.6(GLIBC_2.25)(64bit)
libc.so.6(GLIBC_2.26)(64bit)
libc.so.6(GLIBC_2.27)(64bit)
libc.so.6(GLIBC_2.28)(64bit)

一般有两种依赖，libc.so.6()(64bit) ， libc.so.6(GLIBC_2.28)(64bit) ，2.34 会把 2.33 之前都会提供出来。glibc 这种前向兼容是写的比较好的。



@Pandora 对标下ubuntu2104看看版本，准备分出来一个glibc-2.33-riscv-master





目前态度：

吴伟：

可以啊，10.3+glibc2.33

https://build.opensuse.org/project/show/openSUSE:Factory:RISCV  Version:        7.5.0+r278197



https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/package_manifest/baseos-repository#:~:text=The%20BaseOS%20repository%20Content%20in%20the%20BaseOS%20repository,in%20previous%20releases%20of%20Red%20Hat%20Enterprise%20Linux.



https://build.opensuse.org/project/show/openSUSE:Factory:RISCV



http://fedora.riscv.rocks/kojifiles/packages/gcc/10.3.1/1.fc33/data/logs/riscv64/root.log





---



cxo: D1/oE上安装docker/linux的手把手教程写好了，有人能帮忙验证下不？
https://github.com/mollybuild/RISCV-Measurement/blob/master/install-docker-on-D1-oE-and-run-docker-linux.md



可以啊，10.3+glibc2.33



https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-repo.md
整理了一份第一批76个重点包的清单，有些包在mainline上都没成功过几次。。。
https://build.openeuler.org/project/show/home:yx971:RISC-V:BaseOS

BaseOS里看上感兴趣的也可以branch到个人工程测试

https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-osc-build-tools.md



所有列在

https://github.com/plctlab/openEuler-riscv/blob/main/members.md
中的实习生和社区开发者都可以访问 tarsier-workers 了。

访问方式
全小写你的GitHubID@worker01.tarsier-ci.org



我建立了一个实验性的 OBS：
https://build.tarsier-ci.org/
目前可以开放注册，计划周二左右停止新用户注册
安全防护还没开，有可能推倒重建，请各位使用者做好心理准备

另外
worker01.tarsier-ci.org
worker02.tarsier-ci.org
可以用于OSC本地构建使用



和release sig的人说了一下拉分支的意见，拉分支这个动作影响比较大，他们决策不了，需要上tc会议汇报一下  @王建民



杨昕私人工程：home:yx971:RISC-V:BaseOS



私人工程的话可能无法满足我在生产环境 yum install 的需求。
OK，so 让我们来选择一条hard模式：

1. fork OBS w/ worker
2. fork update site / rpm source
3. fork all src repos

其中 3 和 2 已经有了，我直接复用软件所的。还需要一个 obs server。

等验证好了之后，再批量的往 home:yx971:RISC-V:BaseOS 上提交。





我下周就想办成三件事：

1. D1上的oE跑起来docker，docker里面跑起来ubuntu。让软件所跟RISC-V国际基金会的示范应用项目可以按期PR
2. 图形界面跑起来LXDE或者XFCE，能开个网页或者玩个基于BishengJDK的小游戏
3. 让oE的构建能看起来正常，让oE/RV能够有正常稳定的更新源可以使用。也就是生产环境可以使用 yum update / install

本周要完成的三件事情进展：
1. 验证✅ 一键自动部署脚本
2. 本地源码构建验证✅ 合并到oE源⛔️
3. oe构建修复⛔️ tarsier obs ⛔️ tarsier worker ✅ 
4. 

当然欢迎啊。等我把OBS构建好（

同时，PLCT另一个构建服务是ready的：
https://ci.rvperf.org/
里面的jobs对应在
https://github.com/plctlab/riscv-ci
往 riscv-ci 上 PR 一个脚本就可以自动构建的



https://wiki.tizen.org/OBS_Worker_Docker_image





写了一个小脚本，技术难度是么有的，但是可以看到，一开始看起来要半年完成的工作，是如何用脚本和自动化，一点一点提升效率在3天完成的。

这个脚本自动读取members.md文件，得到各位同学的GitHub账号，抓取pubkeys，提供给 obs-workers 的运维脚本

https://github.com/plctlab/openEuler-riscv/blob/main/scripts/get_pubkeys_from_github.sh

我建立了一个 openEuler for RISC-V 的 slack 欢迎加入。这个 Slack 群组的目的
1. 用各种chatbot实现自动化
2. 以后跟英语国家的人讨论openEUler技术问题。
3. 接收各类github/gitee等消息推送。

主要讨论还是在微信群

https://join.slack.com/t/newworkspace-czj7449/shared_invite/zt-usqnawh3-PaKZFOZmhYlmmYGH9cBN3g

吴洁写了一个每日更新issues汇报的脚本，如果各位同学有兴趣的话可以学习下

https://github.com/plctlab/openEuler-riscv/blob/main/scripts/issue_report/run.py

需求文档可以看

https://github.com/plctlab/openEuler-riscv/issues/21



「吴伟: 20.03 还在支持维护么，20.03 版本有 RISC-V 支持么？」
—————————
好像没有专门的 RISCV 部分。SIG组之前的案例，都是用的 20.03 ，石榴派就是用的这个版本。 



我建立了一个实验性的 OBS：
https://build.tarsier-ci.org/
目前可以开放注册，计划周二左右停止新用户注册
安全防护还没开，有可能推倒重建，请各位使用者做好心理准备

另外
worker01.tarsier-ci.org
worker02.tarsier-ci.org
可以用于OSC本地构建使用

这周我应该能把 code.tarsier-ci.org 做起来，跟 build.tarsier-ci.org 同一个子网，clone速度大概能到百兆

code.tarsier-ci.org 会是一个公开只读的gitlab镜像站





https://build.opensuse.org/package/show/openSUSE:Factory:RISCV/chromium

这里有一个 openSUSE 在尝试构建 Chromium for RISC-V 的例子（还没成功）有兴趣的同学可以凑凑热闹





https://build.openeuler.org/project/show/BaseOS
这里的BaseOS它正常么？
This project does not contain any packages

This project has no subprojects

https://build.openeuler.org/package/live_build_log/home:yx971:RISC-V:BaseOS/automake/BaseOS_Base50/riscv64

昨晚看只有1个build error，看起来是环境问题。

环境还在逐步配置

第一步只有20个包，但是由于mainline触发了重构，一直排队不上worker





目前遇到的本地环境无法安装python3-devel问题和llvm包依赖的valgrind包好像不支持riscv架构的问题
https://github.com/plctlab/openEuler-riscv/issues/19

是指 https://github.com/plctlab/openEuler-riscv/issues/35#issuecomment-908485446 
么

本地时可以把这个源加入 http://119.3.219.20:82/openEuler:/Mainline:/RISC-V/standard_riscv64/

osc默认的源中很多依赖包没有

目前osc没有开自身编译，即使编译成功也不会得到应用

在 Linux 下基本上就按照
https://github.com/plctlab/riscv-ci/blob/main/plct-qemu-nuclei-rebase.sh
然后报什么错误就补什么安装包





大家早上好，我想在下午把依赖仓重新同步一下了，请问大家有什么包想一起同步进来吗（比如webkit2gtk3)？

之前对obs里的unresolvable做了个统计，这些包缺失导致的依赖问题比较多，大家可以关注下

('xmvn', 2310), ('maven-surefire', 1972), ('junit', 1009), ('maven-resources-plugin', 654), ('maven-jar-plugin', 650), ('maven-javadoc-plugin', 649), ('maven-compiler-plugin', 648), ('qt5-qtbase', 401), ('webkit2gtk3', 330), ('maven', 325), ('maven-plugin-bundle', 276), ('ant', 269), ('maven-plugin-tools', 150), ('javapackages-tools', 116), ('slf4j', 107), ('plexus-containers', 102), ('plexus-utils', 91), ('maven-enforcer', 87), ('objectweb-asm', 86), ('sonatype-oss-parent', 85), ('jboss-parent', 84), ('maven-resolver', 76), ('qt', 75), ('maven-parent', 70), ('maven-source-plugin', 70), ('maven2', 68), ('glassfish-servlet-api', 68), ('apache-commons-logging', 67), ('maven-plugin-build-helper', 63), ('maven-antrun-plugin', 63), ('jetty', 56), ('apache-commons-io', 50)

刚刚更新了依赖仓，添加了webkit2gtk3，目前unresolvable的数量是1894，比之前少了200左右