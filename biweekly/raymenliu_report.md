
在2月底加入社区，并在 Windows10/11 下完成了openEuler RISC-V 虚拟机环境的搭建，参考了 gitee 上官方的新手入门和修包流程，初步熟悉OBS平台及osc命令行在OBS平台及本地的RPM包源码编译和问题分析

成功修复本地 openEuler RISC-V Qemu 虚拟机 在 Windows PowerShell 下的启动脚本及虚拟机成功运行后的一些OBS使用环境必备内容的补充（后续将此整合为笔记文档分享）

RISC-V 中间仓 PR：
 . jsoup  
 . jsr305
 . maven
  
   依据OBS分析 3 大 packages 之间相互的 dependencies :

   		包括因JAR包的缺少导致的编译出错，例如：proposedAnnotations:jar、 tcl.jar 、ri.jar

   		缺少的maven插件 例如：maven-compiler-plugin；

下期工作目标：
   发现自身知识库的薄弱之处，加倍学习同学们分享的修包经验，并完善修包笔记文档，
   修复更多自己很少接触的package。