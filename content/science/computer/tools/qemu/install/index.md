---
title: 安装
date: 2026-10-02
---


## termux

安装 qemu
```bash
pkg install qemu-utils
pkg install qemu-system-x86-64 qemu-system-x86-64-headless cdrtools
```

下载 qcow2
```bash
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.qcow2
```

登录修改
```bash
cat > user-data <<'EOF'
#cloud-config
password: debian
chpasswd: { expire: False }
ssh_pwauth: True
EOF
```

生成 iso
```bash
pkg install cdrtools -y
mkisofs -o cloudinit.iso user-data
```

带 cdrom 启动参数
```bash
qemu-system-x86_64 \
-machine pc \
-accel tcg,thread=multi \
-cpu max \
-m 8192 \
-smp 4 \
-drive file=debian-12-generic-amd64.qcow2,format=qcow2,if=virtio \
-cdrom cloudinit.iso \
-netdev user,id=net0,hostfwd=tcp::2222-:22,hostfwd=tcp::8080-:8080 \
-device virtio-net-pci,netdev=net0 \
-nographic
```
