---
title: tree
date: 2026-08-04
series: ["rust 学习记录"]
series_order: 1
---


{{< katex >}}


<details>
<summary> toc </summary>

```bash
├── boot
│   ├── bootsect.s
│   ├── head.s
│   ├── Makefile
│   └── setup.s
├── fs
│   ├── bitmap.c
│   ├── block_dev.c
│   ├── buffer.c
│   ├── char_dev.c
│   ├── exec.c
│   ├── fcntl.c
│   ├── file_dev.c
│   ├── file_table.c
│   ├── inode.c
│   ├── ioctl.c
│   ├── Makefile
│   ├── namei.c
│   ├── open.c
│   ├── pipe.c
│   ├── read_write.c
│   ├── stat.c
│   ├── super.c
│   └── truncate.c
├── hdc-0.11.img
├── include
│   ├── a.out.h
│   ├── asm
│   │   ├── io.h
│   │   ├── memory.h
│   │   ├── segment.h
│   │   └── system.h
│   ├── const.h
│   ├── ctype.h
│   ├── errno.h
│   ├── fcntl.h
│   ├── linux
│   │   ├── config.h
│   │   ├── fdreg.h
│   │   ├── fs.h
│   │   ├── hdreg.h
│   │   ├── head.h
│   │   ├── kernel.h
│   │   ├── mm.h
│   │   ├── sched.h
│   │   ├── sys.h
│   │   └── tty.h
│   ├── signal.h
│   ├── stdarg.h
│   ├── stddef.h
│   ├── string.h
│   ├── sys
│   │   ├── stat.h
│   │   ├── times.h
│   │   ├── types.h
│   │   ├── utsname.h
│   │   └── wait.h
│   ├── termios.h
│   ├── time.h
│   ├── unistd.h
│   └── utime.h
├── init
│   └── main.c
├── kernel
│   ├── asm.s
│   ├── blk_drv
│   │   ├── blk.h
│   │   ├── floppy.c
│   │   ├── hd.c
│   │   ├── ll_rw_blk.c
│   │   ├── Makefile
│   │   └── ramdisk.c
│   ├── chr_drv
│   │   ├── console.c
│   │   ├── kb.S
│   │   ├── Makefile
│   │   ├── rs_io.s
│   │   ├── serial.c
│   │   ├── tty_io.c
│   │   └── tty_ioctl.c
│   ├── exit.c
│   ├── fork.c
│   ├── Makefile
│   ├── math
│   │   ├── Makefile
│   │   └── math_emulate.c
│   ├── mktime.c
│   ├── panic.c
│   ├── printk.c
│   ├── sched.c
│   ├── signal.c
│   ├── sys.c
│   ├── system_call.s
│   ├── traps.c
│   ├── vsprintf.c
│   └── who.c
├── lib
│   ├── close.c
│   ├── ctype.c
│   ├── dup.c
│   ├── errno.c
│   ├── execve.c
│   ├── _exit.c
│   ├── Makefile
│   ├── malloc.c
│   ├── open.c
│   ├── setsid.c
│   ├── string.c
│   ├── wait.c
│   └── write.c
├── Makefile
├── Makefile.header
├── mm
│   ├── Makefile
│   ├── memory.c
│   └── page.s
├── README.md
├── readme.old
├── tools
│   ├── bochs
│   │   ├── bochsrc
│   │   │   ├── bochsrc-hd.bxrc
│   │   │   └── bochsrc-hd-dbg.bxrc
│   │   └── README
│   ├── build.sh
│   ├── gdb
│   └── README
├── tree.md
├── Yu.img
└── YUOEK.md

17 directories, 114 files


```

</details>

