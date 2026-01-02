ctarget:     file format elf64-x86-64


Disassembly of section .init:

0000000000400c48 <_init>:
  400c48:       48 83 ec 08             sub    $0x8,%rsp
  400c4c:       48 8b 05 a5 43 20 00    mov    0x2043a5(%rip),%rax        # 604ff8 <__gmon_start__>
  400c53:       48 85 c0                test   %rax,%rax
  400c56:       74 02                   je     400c5a <_init+0x12>
  400c58:       ff d0                   callq  *%rax
  400c5a:       48 83 c4 08             add    $0x8,%rsp
  400c5e:       c3                      retq

Disassembly of section .plt:

0000000000400c60 <.plt>:
  400c60:       ff 35 a2 43 20 00       pushq  0x2043a2(%rip)        # 605008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400c66:       ff 25 a4 43 20 00       jmpq   *0x2043a4(%rip)        # 605010 <_GLOBAL_OFFSET_TABLE_+0x10>
  400c6c:       0f 1f 40 00             nopl   0x0(%rax)

0000000000400c70 <strcasecmp@plt>:
  402c70:       ff 25 a2 43 20 00       jmpq   *0x2043a2(%rip)        # 605018 <strcasecmp@GLIBC_2.2.5>
  400c76:       68 00 00 00 00          pushq  $0x0
  400c7b:       e9 e0 ff ff ff          jmpq   400c60 <.plt>

0000000000400c80 <__errno_location@plt>:
  400c80:       ff 25 9a 43 20 00       jmpq   *0x20439a(%rip)        # 605020 <__errno_location@GLIBC_2.2.5>
  400c86:       68 01 00 00 00          pushq  $0x1
  400c8b:       e9 d0 ff ff ff          jmpq   400c60 <.plt>

0000000000400c90 <srandom@plt>:
  400c90:       ff 25 92 43 20 00       jmpq   *0x204392(%rip)        # 605028 <srandom@GLIBC_2.2.5>
  400c96:       68 02 00 00 00          pushq  $0x2
  400c9b:       e9 c0 ff ff ff          jmpq   400c60 <.plt>

0000000000400ca0 <strncmp@plt>:
  400ca0:       ff 25 8a 43 20 00       jmpq   *0x20438a(%rip)        # 605030 <strncmp@GLIBC_2.2.5>
  400ca6:       68 03 00 00 00          pushq  $0x3
  400cab:       e9 b0 ff ff ff          jmpq   400c60 <.plt>

0000000000400cb0 <strcpy@plt>:
  400cb0:       ff 25 82 43 20 00       jmpq   *0x204382(%rip)        # 605038 <strcpy@GLIBC_2.2.5>
  400cb6:       68 04 00 00 00          pushq  $0x4
  400cbb:       e9 a0 ff ff ff          jmpq   400c60 <.plt>

0000000000400cc0 <puts@plt>:
  400cc0:       ff 25 7a 43 20 00       jmpq   *0x20437a(%rip)        # 605040 <puts@GLIBC_2.2.5>
  400cc6:       68 05 00 00 00          pushq  $0x5
  400ccb:       e9 90 ff ff ff          jmpq   400c60 <.plt>

0000000000400cd0 <write@plt>:
  400cd0:       ff 25 72 43 20 00       jmpq   *0x204372(%rip)        # 605048 <write@GLIBC_2.2.5>
  400cd6:       68 06 00 00 00          pushq  $0x6
  400cdb:       e9 80 ff ff ff          jmpq   400c60 <.plt>

0000000000400ce0 <__stack_chk_fail@plt>:
  400ce0:       ff 25 6a 43 20 00       jmpq   *0x20436a(%rip)        # 605050 <__stack_chk_fail@GLIBC_2.4>
  400ce6:       68 07 00 00 00          pushq  $0x7
  400ceb:       e9 70 ff ff ff          jmpq   400c60 <.plt>

0000000000400cf0 <mmap@plt>:
  400cf0:       ff 25 62 43 20 00       jmpq   *0x204362(%rip)        # 605058 <mmap@GLIBC_2.2.5>
  400cf6:       68 08 00 00 00          pushq  $0x8
  400cfb:       e9 60 ff ff ff          jmpq   400c60 <.plt>

0000000000400d00 <memset@plt>:
  400d00:       ff 25 5a 43 20 00       jmpq   *0x20435a(%rip)        # 605060 <memset@GLIBC_2.2.5>
  400d06:       68 09 00 00 00          pushq  $0x9
  400d0b:       e9 50 ff ff ff          jmpq   400c60 <.plt>

0000000000400d10 <alarm@plt>:
  400d10:       ff 25 52 43 20 00       jmpq   *0x204352(%rip)        # 605068 <alarm@GLIBC_2.2.5>
  400d16:       68 0a 00 00 00          pushq  $0xa
  400d1b:       e9 40 ff ff ff          jmpq   400c60 <.plt>

0000000000400d20 <close@plt>:
  400d20:       ff 25 4a 43 20 00       jmpq   *0x20434a(%rip)        # 605070 <close@GLIBC_2.2.5>
  400d26:       68 0b 00 00 00          pushq  $0xb
  400d2b:       e9 30 ff ff ff          jmpq   400c60 <.plt>

0000000000400d30 <read@plt>:
  400d30:       ff 25 42 43 20 00       jmpq   *0x204342(%rip)        # 605078 <read@GLIBC_2.2.5>
  400d36:       68 0c 00 00 00          pushq  $0xc
  400d3b:       e9 20 ff ff ff          jmpq   400c60 <.plt>

0000000000400d40 <signal@plt>:
  400d40:       ff 25 3a 43 20 00       jmpq   *0x20433a(%rip)        # 605080 <signal@GLIBC_2.2.5>
  400d46:       68 0d 00 00 00          pushq  $0xd
  400d4b:       e9 10 ff ff ff          jmpq   400c60 <.plt>

0000000000400d50 <gethostbyname@plt>:
  400d50:       ff 25 32 43 20 00       jmpq   *0x204332(%rip)        # 605088 <gethostbyname@GLIBC_2.2.5>
  400d56:       68 0e 00 00 00          pushq  $0xe
  400d5b:       e9 00 ff ff ff          jmpq   400c60 <.plt>

0000000000400d60 <__memmove_chk@plt>:
  400d60:       ff 25 2a 43 20 00       jmpq   *0x20432a(%rip)        # 605090 <__memmove_chk@GLIBC_2.3.4>
  400d66:       68 0f 00 00 00          pushq  $0xf
  400d6b:       e9 f0 fe ff ff          jmpq   400c60 <.plt>

0000000000400d70 <strtol@plt>:
  400d70:       ff 25 22 43 20 00       jmpq   *0x204322(%rip)        # 605098 <strtol@GLIBC_2.2.5>
  400d76:       68 10 00 00 00          pushq  $0x10
  400d7b:       e9 e0 fe ff ff          jmpq   400c60 <.plt>

0000000000400d80 <memcpy@plt>:
  400d80:       ff 25 1a 43 20 00       jmpq   *0x20431a(%rip)        # 6050a0 <memcpy@GLIBC_2.14>
  400d86:       68 11 00 00 00          pushq  $0x11
  400d8b:       e9 d0 fe ff ff          jmpq   400c60 <.plt>

0000000000400d90 <time@plt>:
  400d90:       ff 25 12 43 20 00       jmpq   *0x204312(%rip)        # 6050a8 <time@GLIBC_2.2.5>
  400d96:       68 12 00 00 00          pushq  $0x12
  400d9b:       e9 c0 fe ff ff          jmpq   400c60 <.plt>

0000000000400da0 <random@plt>:
  400da0:       ff 25 0a 43 20 00       jmpq   *0x20430a(%rip)        # 6050b0 <random@GLIBC_2.2.5>
  400da6:       68 13 00 00 00          pushq  $0x13
  400dab:       e9 b0 fe ff ff          jmpq   400c60 <.plt>

0000000000400db0 <_IO_getc@plt>:
  400db0:       ff 25 02 43 20 00       jmpq   *0x204302(%rip)        # 6050b8 <_IO_getc@GLIBC_2.2.5>
  400db6:       68 14 00 00 00          pushq  $0x14
  400dbb:       e9 a0 fe ff ff          jmpq   400c60 <.plt>

0000000000400dc0 <__isoc99_sscanf@plt>:
  400dc0:       ff 25 fa 42 20 00       jmpq   *0x2042fa(%rip)        # 6050c0 <__isoc99_sscanf@GLIBC_2.7>
  400dc6:       68 15 00 00 00          pushq  $0x15
  400dcb:       e9 90 fe ff ff          jmpq   400c60 <.plt>

0000000000400dd0 <munmap@plt>:
  400dd0:       ff 25 f2 42 20 00       jmpq   *0x2042f2(%rip)        # 6050c8 <munmap@GLIBC_2.2.5>
  400dd6:       68 16 00 00 00          pushq  $0x16
  400ddb:       e9 80 fe ff ff          jmpq   400c60 <.plt>

0000000000400de0 <__printf_chk@plt>:
  400de0:       ff 25 ea 42 20 00       jmpq   *0x2042ea(%rip)        # 6050d0 <__printf_chk@GLIBC_2.3.4>
  400de6:       68 17 00 00 00          pushq  $0x17
  400deb:       e9 70 fe ff ff          jmpq   400c60 <.plt>

0000000000400df0 <fopen@plt>:
  400df0:       ff 25 e2 42 20 00       jmpq   *0x2042e2(%rip)        # 6050d8 <fopen@GLIBC_2.2.5>
  400df6:       68 18 00 00 00          pushq  $0x18
  400dfb:       e9 60 fe ff ff          jmpq   400c60 <.plt>

0000000000400e00 <getopt@plt>:
  400e00:       ff 25 da 42 20 00       jmpq   *0x2042da(%rip)        # 6050e0 <getopt@GLIBC_2.2.5>
  400e06:       68 19 00 00 00          pushq  $0x19
  400e0b:       e9 50 fe ff ff          jmpq   400c60 <.plt>

0000000000400e10 <strtoul@plt>:
  400e10:       ff 25 d2 42 20 00       jmpq   *0x2042d2(%rip)        # 6050e8 <strtoul@GLIBC_2.2.5>
  400e16:       68 1a 00 00 00          pushq  $0x1a
  400e1b:       e9 40 fe ff ff          jmpq   400c60 <.plt>

0000000000400e20 <gethostname@plt>:
  400e20:       ff 25 ca 42 20 00       jmpq   *0x2042ca(%rip)        # 6050f0 <gethostname@GLIBC_2.2.5>
  400e26:       68 1b 00 00 00          pushq  $0x1b
  400e2b:       e9 30 fe ff ff          jmpq   400c60 <.plt>

0000000000400e30 <exit@plt>:
  400e30:       ff 25 c2 42 20 00       jmpq   *0x2042c2(%rip)        # 6050f8 <exit@GLIBC_2.2.5>
  400e36:       68 1c 00 00 00          pushq  $0x1c
  400e3b:       e9 20 fe ff ff          jmpq   400c60 <.plt>

0000000000400e40 <connect@plt>:
  400e40:       ff 25 ba 42 20 00       jmpq   *0x2042ba(%rip)        # 605100 <connect@GLIBC_2.2.5>
  400e46:       68 1d 00 00 00          pushq  $0x1d
  400e4b:       e9 10 fe ff ff          jmpq   400c60 <.plt>

0000000000400e50 <__fprintf_chk@plt>:
  400e50:       ff 25 b2 42 20 00       jmpq   *0x2042b2(%rip)        # 605108 <__fprintf_chk@GLIBC_2.3.4>
  400e56:       68 1e 00 00 00          pushq  $0x1e
  400e5b:       e9 00 fe ff ff          jmpq   400c60 <.plt>

0000000000400e60 <__sprintf_chk@plt>:
  400e60:       ff 25 aa 42 20 00       jmpq   *0x2042aa(%rip)        # 605110 <__sprintf_chk@GLIBC_2.3.4>
  400e66:       68 1f 00 00 00          pushq  $0x1f
  400e6b:       e9 f0 fd ff ff          jmpq   400c60 <.plt>

0000000000400e70 <socket@plt>:
  400e70:       ff 25 a2 42 20 00       jmpq   *0x2042a2(%rip)        # 605118 <socket@GLIBC_2.2.5>
  400e76:       68 20 00 00 00          pushq  $0x20
  400e7b:       e9 e0 fd ff ff          jmpq   400c60 <.plt>

Disassembly of section .text:

0000000000400e80 <_start>:
  400e80:       31 ed                   xor    %ebp,%ebp
  400e82:       49 89 d1                mov    %rdx,%r9
  400e85:       5e                      pop    %rsi
  400e86:       48 89 e2                mov    %rsp,%rdx
  400e89:       48 83 e4 f0             and    $0xfffffffffffffff0,%rsp
  400e8d:       50                      push   %rax
  400e8e:       54                      push   %rsp
  400e8f:       49 c7 c0 60 2f 40 00    mov    $0x402f60,%r8
  400e96:       48 c7 c1 f0 2e 40 00    mov    $0x402ef0,%rcx
  400e9d:       48 c7 c7 b0 11 40 00    mov    $0x4011b0,%rdi
  400ea4:       ff 15 46 41 20 00       callq  *0x204146(%rip)        # 604ff0 <__libc_start_main@GLIBC_2.2.5>
  400eaa:       f4                      hlt
  400eab:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000400eb0 <_dl_relocate_static_pie>:
  400eb0:       f3 c3                   repz retq
  400eb2:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  400eb9:       00 00 00
  400ebc:       0f 1f 40 00             nopl   0x0(%rax)

0000000000400ec0 <deregister_tm_clones>:
  400ec0:       b8 97 54 60 00          mov    $0x605497,%eax
  400ec5:       55                      push   %rbp
  400ec6:       48 2d 90 54 60 00       sub    $0x605490,%rax
  400ecc:       48 83 f8 0e             cmp    $0xe,%rax
  400ed0:       48 89 e5                mov    %rsp,%rbp
  400ed3:       76 1b                   jbe    400ef0 <deregister_tm_clones+0x30>
  400ed5:       b8 00 00 00 00          mov    $0x0,%eax
  400eda:       48 85 c0                test   %rax,%rax
  400edd:       74 11                   je     400ef0 <deregister_tm_clones+0x30>
  400edf:       5d                      pop    %rbp
  400ee0:       bf 90 54 60 00          mov    $0x605490,%edi
  400ee5:       ff e0                   jmpq   *%rax
  400ee7:       66 0f 1f 84 00 00 00    nopw   0x0(%rax,%rax,1)
  400eee:       00 00
  400ef0:       5d                      pop    %rbp
  400ef1:       c3                      retq
  400ef2:       0f 1f 40 00             nopl   0x0(%rax)
  400ef6:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  400efd:       00 00 00

0000000000400f00 <register_tm_clones>:
  400f00:       be 90 54 60 00          mov    $0x605490,%esi
  400f05:       55                      push   %rbp
  400f06:       48 81 ee 90 54 60 00    sub    $0x605490,%rsi
  400f0d:       48 c1 fe 03             sar    $0x3,%rsi
  400f11:       48 89 e5                mov    %rsp,%rbp
  400f14:       48 89 f0                mov    %rsi,%rax
  400f17:       48 c1 e8 3f             shr    $0x3f,%rax
  400f1b:       48 01 c6                add    %rax,%rsi
  400f1e:       48 d1 fe                sar    %rsi
  400f21:       74 15                   je     400f38 <register_tm_clones+0x38>
  400f23:       b8 00 00 00 00          mov    $0x0,%eax
  400f28:       48 85 c0                test   %rax,%rax
  400f2b:       74 0b                   je     400f38 <register_tm_clones+0x38>
  400f2d:       5d                      pop    %rbp
  400f2e:       bf 90 54 60 00          mov    $0x605490,%edi
  400f33:       ff e0                   jmpq   *%rax
  400f35:       0f 1f 00                nopl   (%rax)
  400f38:       5d                      pop    %rbp
  400f39:       c3                      retq
  400f3a:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)

0000000000400f40 <__do_global_dtors_aux>:
  400f40:       80 3d 81 45 20 00 00    cmpb   $0x0,0x204581(%rip)        # 6054c8 <completed.7667>
  400f47:       75 11                   jne    400f5a <__do_global_dtors_aux+0x1a>
  400f49:       55                      push   %rbp
  400f4a:       48 89 e5                mov    %rsp,%rbp
  400f4d:       e8 6e ff ff ff          callq  400ec0 <deregister_tm_clones>
  400f52:       5d                      pop    %rbp
  400f53:       c6 05 6e 45 20 00 01    movb   $0x1,0x20456e(%rip)        # 6054c8 <completed.7667>
  400f5a:       f3 c3                   repz retq
  400f5c:       0f 1f 40 00             nopl   0x0(%rax)

0000000000400f60 <frame_dummy>:
  400f60:       bf 18 4e 60 00          mov    $0x604e18,%edi
  400f65:       48 83 3f 00             cmpq   $0x0,(%rdi)
  400f69:       75 05                   jne    400f70 <frame_dummy+0x10>
  400f6b:       eb 93                   jmp    400f00 <register_tm_clones>
  400f6d:       0f 1f 00                nopl   (%rax)
  400f70:       b8 00 00 00 00          mov    $0x0,%eax
  400f75:       48 85 c0                test   %rax,%rax
  400f78:       74 f1                   je     400f6b <frame_dummy+0xb>
  400f7a:       55                      push   %rbp
  400f7b:       48 89 e5                mov    %rsp,%rbp
  400f7e:       ff d0                   callq  *%rax
  400f80:       5d                      pop    %rbp
  400f81:       e9 7a ff ff ff          jmpq   400f00 <register_tm_clones>

0000000000400f86 <usage>:
  400f86:       48 83 ec 08             sub    $0x8,%rsp
  400f8a:       48 89 fa                mov    %rdi,%rdx
  400f8d:       83 3d 74 45 20 00 00    cmpl   $0x0,0x204574(%rip)        # 605508 <is_checker>
  400f94:       74 48                   je     400fde <usage+0x58>
  400f96:       48 8d 35 db 1f 00 00    lea    0x1fdb(%rip),%rsi        # 402f78 <_IO_stdin_used+0x8>
  400f9d:       bf 01 00 00 00          mov    $0x1,%edi
  400fa2:       b8 00 00 00 00          mov    $0x0,%eax
  400fa7:       e8 34 fe ff ff          callq  400de0 <__printf_chk@plt>
  400fac:       48 8d 3d fd 1f 00 00    lea    0x1ffd(%rip),%rdi        # 402fb0 <_IO_stdin_used+0x40>
  400fb3:       e8 08 fd ff ff          callq  400cc0 <puts@plt>
  400fb8:       48 8d 3d 69 21 00 00    lea    0x2169(%rip),%rdi        # 403128 <_IO_stdin_used+0x1b8>
  400fbf:       e8 fc fc ff ff          callq  400cc0 <puts@plt>
  400fc4:       48 8d 3d 0d 20 00 00    lea    0x200d(%rip),%rdi        # 402fd8 <_IO_stdin_used+0x68>
  400fcb:       e8 f0 fc ff ff          callq  400cc0 <puts@plt>
  400fd0:       48 8d 3d 6b 21 00 00    lea    0x216b(%rip),%rdi        # 403142 <_IO_stdin_used+0x1d2>
  400fd7:       e8 e4 fc ff ff          callq  400cc0 <puts@plt>
  400fdc:       eb 3a                   jmp    401018 <usage+0x92>
  400fde:       48 8d 35 79 21 00 00    lea    0x2179(%rip),%rsi        # 40315e <_IO_stdin_used+0x1ee>
  400fe5:       bf 01 00 00 00          mov    $0x1,%edi
  400fea:       b8 00 00 00 00          mov    $0x0,%eax
  400fef:       e8 ec fd ff ff          callq  400de0 <__printf_chk@plt>
  400ff4:       48 8d 3d 05 20 00 00    lea    0x2005(%rip),%rdi        # 403000 <_IO_stdin_used+0x90>
  400ffb:       e8 c0 fc ff ff          callq  400cc0 <puts@plt>
  401000:       48 8d 3d 21 20 00 00    lea    0x2021(%rip),%rdi        # 403028 <_IO_stdin_used+0xb8>
  401007:       e8 b4 fc ff ff          callq  400cc0 <puts@plt>
  40100c:       48 8d 3d 69 21 00 00    lea    0x2169(%rip),%rdi        # 40317c <_IO_stdin_used+0x20c>
  401013:       e8 a8 fc ff ff          callq  400cc0 <puts@plt>
  401018:       bf 00 00 00 00          mov    $0x0,%edi
  40101d:       e8 0e fe ff ff          callq  400e30 <exit@plt>

0000000000401022 <initialize_target>:
  401022:       55                      push   %rbp
  401023:       53                      push   %rbx
  401024:       48 81 ec 18 21 00 00    sub    $0x2118,%rsp
  40102b:       89 f5                   mov    %esi,%ebp
  40102d:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  401034:       00 00
  401036:       48 89 84 24 08 21 00    mov    %rax,0x2108(%rsp)
  40103d:       00
  40103e:       31 c0                   xor    %eax,%eax
  401040:       89 3d b2 44 20 00       mov    %edi,0x2044b2(%rip)        # 6054f8 <check_level>
  401046:       8b 3d e4 40 20 00       mov    0x2040e4(%rip),%edi        # 605130 <target_id>
  40104c:       e8 79 1e 00 00          callq  402eca <gencookie>
  401051:       89 05 ad 44 20 00       mov    %eax,0x2044ad(%rip)        # 605504 <cookie>
  401057:       89 c7                   mov    %eax,%edi
  401059:       e8 6c 1e 00 00          callq  402eca <gencookie>
  40105e:       89 05 9c 44 20 00       mov    %eax,0x20449c(%rip)        # 605500 <authkey>
  401064:       8b 05 c6 40 20 00       mov    0x2040c6(%rip),%eax        # 605130 <target_id>
  40106a:       8d 78 01                lea    0x1(%rax),%edi
  40106d:       e8 1e fc ff ff          callq  400c90 <srandom@plt>
  401072:       e8 29 fd ff ff          callq  400da0 <random@plt>
  401077:       89 c7                   mov    %eax,%edi
  401079:       e8 2b 03 00 00          callq  4013a9 <scramble>
  40107e:       89 c3                   mov    %eax,%ebx
  401080:       85 ed                   test   %ebp,%ebp
  401082:       74 18                   je     40109c <initialize_target+0x7a>
  401084:       bf 00 00 00 00          mov    $0x0,%edi
  401089:       e8 02 fd ff ff          callq  400d90 <time@plt>
  40108e:       89 c7                   mov    %eax,%edi
  401090:       e8 fb fb ff ff          callq  400c90 <srandom@plt>
  401095:       e8 06 fd ff ff          callq  400da0 <random@plt>
  40109a:       eb 05                   jmp    4010a1 <initialize_target+0x7f>
  40109c:       b8 00 00 00 00          mov    $0x0,%eax
  4010a1:       01 c3                   add    %eax,%ebx
  4010a3:       0f b7 db                movzwl %bx,%ebx
  4010a6:       8d 04 dd 00 01 00 00    lea    0x100(,%rbx,8),%eax
  4010ad:       89 c0                   mov    %eax,%eax
  4010af:       48 89 05 ca 43 20 00    mov    %rax,0x2043ca(%rip)        # 605480 <buf_offset>
  4010b6:       c6 05 6b 50 20 00 63    movb   $0x63,0x20506b(%rip)        # 606128 <target_prefix>
  4010bd:       83 3d c4 43 20 00 00    cmpl   $0x0,0x2043c4(%rip)        # 605488 <notify>
  4010c4:       0f 84 c4 00 00 00       je     40118e <initialize_target+0x16c>
  4010ca:       83 3d 37 44 20 00 00    cmpl   $0x0,0x204437(%rip)        # 605508 <is_checker>
  4010d1:       0f 85 b7 00 00 00       jne    40118e <initialize_target+0x16c>
  4010d7:       48 89 e7                mov    %rsp,%rdi
  4010da:       be 00 01 00 00          mov    $0x100,%esi
  4010df:       e8 3c fd ff ff          callq  400e20 <gethostname@plt>
  4010e4:       85 c0                   test   %eax,%eax
  4010e6:       74 27                   je     40110f <initialize_target+0xed>
  4010e8:       48 8d 3d 69 1f 00 00    lea    0x1f69(%rip),%rdi        # 403058 <_IO_stdin_used+0xe8>
  4010ef:       e8 cc fb ff ff          callq  400cc0 <puts@plt>
  4010f4:       bf 08 00 00 00          mov    $0x8,%edi
  4010f9:       e8 32 fd ff ff          callq  400e30 <exit@plt>
  4010fe:       48 89 e6                mov    %rsp,%rsi
  401101:       e8 6a fb ff ff          callq  400c70 <strcasecmp@plt>
  401106:       85 c0                   test   %eax,%eax
  401108:       74 24                   je     40112e <initialize_target+0x10c>
  40110a:       83 c3 01                add    $0x1,%ebx
  40110d:       eb 05                   jmp    401114 <initialize_target+0xf2>
  40110f:       bb 00 00 00 00          mov    $0x0,%ebx
  401114:       48 63 c3                movslq %ebx,%rax
  401117:       48 8d 15 42 40 20 00    lea    0x204042(%rip),%rdx        # 605160 <host_table>
  40111e:       48 8b 3c c2             mov    (%rdx,%rax,8),%rdi
  401122:       48 85 ff                test   %rdi,%rdi
  401125:       75 d7                   jne    4010fe <initialize_target+0xdc>
  401127:       b8 00 00 00 00          mov    $0x0,%eax
  40112c:       eb 05                   jmp    401133 <initialize_target+0x111>
  40112e:       b8 01 00 00 00          mov    $0x1,%eax
  401133:       85 c0                   test   %eax,%eax
  401135:       75 1e                   jne    401155 <initialize_target+0x133>
  401137:       48 89 e2                mov    %rsp,%rdx
  40113a:       48 8d 35 4f 1f 00 00    lea    0x1f4f(%rip),%rsi        # 403090 <_IO_stdin_used+0x120>
  401141:       bf 01 00 00 00          mov    $0x1,%edi
  401146:       e8 95 fc ff ff          callq  400de0 <__printf_chk@plt>
  40114b:       bf 08 00 00 00          mov    $0x8,%edi
  401150:       e8 db fc ff ff          callq  400e30 <exit@plt>
  401155:       48 8d bc 24 00 01 00    lea    0x100(%rsp),%rdi
  40115c:       00
  40115d:       e8 c8 1a 00 00          callq  402c2a <init_driver>
  401162:       85 c0                   test   %eax,%eax
  401164:       79 28                   jns    40118e <initialize_target+0x16c>
  401166:       48 8d 94 24 00 01 00    lea    0x100(%rsp),%rdx
  40116d:       00
  40116e:       48 8d 35 5b 1f 00 00    lea    0x1f5b(%rip),%rsi        # 4030d0 <_IO_stdin_used+0x160>
  401175:       bf 01 00 00 00          mov    $0x1,%edi
  40117a:       b8 00 00 00 00          mov    $0x0,%eax
  40117f:       e8 5c fc ff ff          callq  400de0 <__printf_chk@plt>
  401184:       bf 08 00 00 00          mov    $0x8,%edi
  401189:       e8 a2 fc ff ff          callq  400e30 <exit@plt>
  40118e:       48 8b 84 24 08 21 00    mov    0x2108(%rsp),%rax
  401195:       00
  401196:       64 48 33 04 25 28 00    xor    %fs:0x28,%rax
  40119d:       00 00
  40119f:       74 05                   je     4011a6 <initialize_target+0x184>
  4011a1:       e8 3a fb ff ff          callq  400ce0 <__stack_chk_fail@plt>
  4011a6:       48 81 c4 18 21 00 00    add    $0x2118,%rsp
  4011ad:       5b                      pop    %rbx
  4011ae:       5d                      pop    %rbp
  4011af:       c3                      retq

00000000004011b0 <main>:
  4011b0:       41 56                   push   %r14
  4011b2:       41 55                   push   %r13
  4011b4:       41 54                   push   %r12
  4011b6:       55                      push   %rbp
  4011b7:       53                      push   %rbx
  4011b8:       41 89 fc                mov    %edi,%r12d
  4011bb:       48 89 f3                mov    %rsi,%rbx
  4011be:       48 c7 c6 65 1f 40 00    mov    $0x401f65,%rsi
  4011c5:       bf 0b 00 00 00          mov    $0xb,%edi
  4011ca:       e8 71 fb ff ff          callq  400d40 <signal@plt>
  4011cf:       48 c7 c6 11 1f 40 00    mov    $0x401f11,%rsi
  4011d6:       bf 07 00 00 00          mov    $0x7,%edi
  4011db:       e8 60 fb ff ff          callq  400d40 <signal@plt>
  4011e0:       48 c7 c6 b9 1f 40 00    mov    $0x401fb9,%rsi
  4011e7:       bf 04 00 00 00          mov    $0x4,%edi
  4011ec:       e8 4f fb ff ff          callq  400d40 <signal@plt>
  4011f1:       83 3d 10 43 20 00 00    cmpl   $0x0,0x204310(%rip)        # 605508 <is_checker>
  4011f8:       74 24                   je     40121e <main+0x6e>
  4011fa:       48 c7 c6 0d 20 40 00    mov    $0x40200d,%rsi
  401201:       bf 0e 00 00 00          mov    $0xe,%edi
  401206:       e8 35 fb ff ff          callq  400d40 <signal@plt>
  40120b:       bf 05 00 00 00          mov    $0x5,%edi
  401210:       e8 fb fa ff ff          callq  400d10 <alarm@plt>
  401215:       48 8d 2d 7e 1f 00 00    lea    0x1f7e(%rip),%rbp        # 40319a <_IO_stdin_used+0x22a>
  40121c:       eb 07                   jmp    401225 <main+0x75>
  40121e:       48 8d 2d 70 1f 00 00    lea    0x1f70(%rip),%rbp        # 403195 <_IO_stdin_used+0x225>
  401225:       48 8b 05 74 42 20 00    mov    0x204274(%rip),%rax        # 6054a0 <stdin@@GLIBC_2.2.5>
  40122c:       48 89 05 bd 42 20 00    mov    %rax,0x2042bd(%rip)        # 6054f0 <infile>
  401233:       41 bd 00 00 00 00       mov    $0x0,%r13d
  401239:       41 be 00 00 00 00       mov    $0x0,%r14d
  40123f:       e9 d5 00 00 00          jmpq   401319 <main+0x169>
  401244:       83 e8 61                sub    $0x61,%eax
  401247:       3c 10                   cmp    $0x10,%al
  401249:       0f 87 a9 00 00 00       ja     4012f8 <main+0x148>
  40124f:       0f b6 c0                movzbl %al,%eax
  401252:       48 8d 0d 87 1f 00 00    lea    0x1f87(%rip),%rcx        # 4031e0 <_IO_stdin_used+0x270>
  401259:       48 63 04 81             movslq (%rcx,%rax,4),%rax
  40125d:       48 01 c1                add    %rax,%rcx
  401260:       ff e1                   jmpq   *%rcx
  401262:       48 8b 3b                mov    (%rbx),%rdi
  401265:       e8 1c fd ff ff          callq  400f86 <usage>
  40126a:       48 8d 35 bc 21 00 00    lea    0x21bc(%rip),%rsi        # 40342d <_IO_stdin_used+0x4bd>
  401271:       48 8b 3d 30 42 20 00    mov    0x204230(%rip),%rdi        # 6054a8 <optarg@@GLIBC_2.2.5>
  401278:       e8 73 fb ff ff          callq  400df0 <fopen@plt>
  40127d:       48 89 05 6c 42 20 00    mov    %rax,0x20426c(%rip)        # 6054f0 <infile>
  401284:       48 85 c0                test   %rax,%rax
  401287:       0f 85 8c 00 00 00       jne    401319 <main+0x169>
  40128d:       48 8b 0d 14 42 20 00    mov    0x204214(%rip),%rcx        # 6054a8 <optarg@@GLIBC_2.2.5>
  401294:       48 8d 15 07 1f 00 00    lea    0x1f07(%rip),%rdx        # 4031a2 <_IO_stdin_used+0x232>
  40129b:       be 01 00 00 00          mov    $0x1,%esi
  4012a0:       48 8b 3d 19 42 20 00    mov    0x204219(%rip),%rdi        # 6054c0 <stderr@@GLIBC_2.2.5>
  4012a7:       e8 a4 fb ff ff          callq  400e50 <__fprintf_chk@plt>
  4012ac:       b8 01 00 00 00          mov    $0x1,%eax
  4012b1:       e9 ea 00 00 00          jmpq   4013a0 <main+0x1f0>
  4012b6:       ba 10 00 00 00          mov    $0x10,%edx
  4012bb:       be 00 00 00 00          mov    $0x0,%esi
  4012c0:       48 8b 3d e1 41 20 00    mov    0x2041e1(%rip),%rdi        # 6054a8 <optarg@@GLIBC_2.2.5>
  4012c7:       e8 44 fb ff ff          callq  400e10 <strtoul@plt>
  4012cc:       41 89 c6                mov    %eax,%r14d
  4012cf:       eb 48                   jmp    401319 <main+0x169>
  4012d1:       ba 0a 00 00 00          mov    $0xa,%edx
  4012d6:       be 00 00 00 00          mov    $0x0,%esi
  4012db:       48 8b 3d c6 41 20 00    mov    0x2041c6(%rip),%rdi        # 6054a8 <optarg@@GLIBC_2.2.5>
  4012e2:       e8 89 fa ff ff          callq  400d70 <strtol@plt>
  4012e7:       41 89 c5                mov    %eax,%r13d
  4012ea:       eb 2d                   jmp    401319 <main+0x169>
  4012ec:       c7 05 92 41 20 00 00    movl   $0x0,0x204192(%rip)        # 605488 <notify>
  4012f3:       00 00 00
  4012f6:       eb 21                   jmp    401319 <main+0x169>
  4012f8:       0f be d2                movsbl %dl,%edx
  4012fb:       48 8d 35 bd 1e 00 00    lea    0x1ebd(%rip),%rsi        # 4031bf <_IO_stdin_used+0x24f>
  401302:       bf 01 00 00 00          mov    $0x1,%edi
  401307:       b8 00 00 00 00          mov    $0x0,%eax
  40130c:       e8 cf fa ff ff          callq  400de0 <__printf_chk@plt>
  401311:       48 8b 3b                mov    (%rbx),%rdi
  401314:       e8 6d fc ff ff          callq  400f86 <usage>
  401319:       48 89 ea                mov    %rbp,%rdx
  40131c:       48 89 de                mov    %rbx,%rsi
  40131f:       44 89 e7                mov    %r12d,%edi
  401322:       e8 d9 fa ff ff          callq  400e00 <getopt@plt>
  401327:       89 c2                   mov    %eax,%edx
  401329:       3c ff                   cmp    $0xff,%al
  40132b:       0f 85 13 ff ff ff       jne    401244 <main+0x94>
  401331:       be 00 00 00 00          mov    $0x0,%esi
  401336:       44 89 ef                mov    %r13d,%edi
  401339:       e8 e4 fc ff ff          callq  401022 <initialize_target>
  40133e:       83 3d c3 41 20 00 00    cmpl   $0x0,0x2041c3(%rip)        # 605508 <is_checker>
  401345:       74 2c                   je     401373 <main+0x1c3>
  401347:       44 3b 35 b2 41 20 00    cmp    0x2041b2(%rip),%r14d        # 605500 <authkey>
  40134e:       74 23                   je     401373 <main+0x1c3>
  401350:       44 89 f2                mov    %r14d,%edx
  401353:       48 8d 35 9e 1d 00 00    lea    0x1d9e(%rip),%rsi        # 4030f8 <_IO_stdin_used+0x188>
  40135a:       bf 01 00 00 00          mov    $0x1,%edi
  40135f:       b8 00 00 00 00          mov    $0x0,%eax
  401364:       e8 77 fa ff ff          callq  400de0 <__printf_chk@plt>
  401369:       b8 00 00 00 00          mov    $0x0,%eax
  40136e:       e8 0f 08 00 00          callq  401b82 <check_fail>
  401373:       8b 15 8b 41 20 00       mov    0x20418b(%rip),%edx        # 605504 <cookie>
  401379:       48 8d 35 52 1e 00 00    lea    0x1e52(%rip),%rsi        # 4031d2 <_IO_stdin_used+0x262>
  401380:       bf 01 00 00 00          mov    $0x1,%edi
  401385:       b8 00 00 00 00          mov    $0x0,%eax
  40138a:       e8 51 fa ff ff          callq  400de0 <__printf_chk@plt>
  40138f:       48 8b 3d ea 40 20 00    mov    0x2040ea(%rip),%rdi        # 605480 <buf_offset>
  401396:       e8 7c 0d 00 00          callq  402117 <stable_launch>
  40139b:       b8 00 00 00 00          mov    $0x0,%eax
  4013a0:       5b                      pop    %rbx
  4013a1:       5d                      pop    %rbp
  4013a2:       41 5c                   pop    %r12
  4013a4:       41 5d                   pop    %r13
  4013a6:       41 5e                   pop    %r14
  4013a8:       c3                      retq

00000000004013a9 <scramble>:
  4013a9:       48 83 ec 38             sub    $0x38,%rsp
  4013ad:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4013b4:       00 00
  4013b6:       48 89 44 24 28          mov    %rax,0x28(%rsp)
  4013bb:       31 c0                   xor    %eax,%eax
  4013bd:       eb 10                   jmp    4013cf <scramble+0x26>
  4013bf:       69 d0 f9 eb 00 00       imul   $0xebf9,%eax,%edx
  4013c5:       01 fa                   add    %edi,%edx
  4013c7:       89 c1                   mov    %eax,%ecx
  4013c9:       89 14 8c                mov    %edx,(%rsp,%rcx,4)
  4013cc:       83 c0 01                add    $0x1,%eax
  4013cf:       83 f8 09                cmp    $0x9,%eax
  4013d2:       76 eb                   jbe    4013bf <scramble+0x16>
  4013d4:       8b 04 24                mov    (%rsp),%eax
  4013d7:       69 c0 39 80 00 00       imul   $0x8039,%eax,%eax
  4013dd:       89 04 24                mov    %eax,(%rsp)
  4013e0:       8b 44 24 18             mov    0x18(%rsp),%eax
  4013e4:       69 c0 eb ce 00 00       imul   $0xceeb,%eax,%eax
  4013ea:       89 44 24 18             mov    %eax,0x18(%rsp)
  4013ee:       8b 44 24 10             mov    0x10(%rsp),%eax
  4013f2:       69 c0 29 a7 00 00       imul   $0xa729,%eax,%eax
  4013f8:       89 44 24 10             mov    %eax,0x10(%rsp)
  4013fc:       8b 44 24 24             mov    0x24(%rsp),%eax
  401400:       69 c0 4a ae 00 00       imul   $0xae4a,%eax,%eax
  401406:       89 44 24 24             mov    %eax,0x24(%rsp)
  40140a:       8b 44 24 04             mov    0x4(%rsp),%eax
  40140e:       69 c0 c6 13 00 00       imul   $0x13c6,%eax,%eax
  401414:       89 44 24 04             mov    %eax,0x4(%rsp)
  401418:       8b 44 24 0c             mov    0xc(%rsp),%eax
  40141c:       69 c0 cd f8 00 00       imul   $0xf8cd,%eax,%eax
  401422:       89 44 24 0c             mov    %eax,0xc(%rsp)
  401426:       8b 44 24 18             mov    0x18(%rsp),%eax
  40142a:       69 c0 35 d0 00 00       imul   $0xd035,%eax,%eax
  401430:       89 44 24 18             mov    %eax,0x18(%rsp)
  401434:       8b 44 24 10             mov    0x10(%rsp),%eax
  401438:       69 c0 59 a9 00 00       imul   $0xa959,%eax,%eax
  40143e:       89 44 24 10             mov    %eax,0x10(%rsp)
  401442:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  401446:       69 c0 47 87 00 00       imul   $0x8747,%eax,%eax
  40144c:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  401450:       8b 44 24 24             mov    0x24(%rsp),%eax
  401454:       69 c0 ab b9 00 00       imul   $0xb9ab,%eax,%eax
  40145a:       89 44 24 24             mov    %eax,0x24(%rsp)
  40145e:       8b 44 24 10             mov    0x10(%rsp),%eax
  401462:       69 c0 71 d2 00 00       imul   $0xd271,%eax,%eax
  401468:       89 44 24 10             mov    %eax,0x10(%rsp)
  40146c:       8b 04 24                mov    (%rsp),%eax
  40146f:       69 c0 b8 38 00 00       imul   $0x38b8,%eax,%eax
  401475:       89 04 24                mov    %eax,(%rsp)
  401478:       8b 44 24 20             mov    0x20(%rsp),%eax
  40147c:       69 c0 7a 44 00 00       imul   $0x447a,%eax,%eax
  401482:       89 44 24 20             mov    %eax,0x20(%rsp)
  401486:       8b 44 24 18             mov    0x18(%rsp),%eax
  40148a:       69 c0 24 12 00 00       imul   $0x1224,%eax,%eax
  401490:       89 44 24 18             mov    %eax,0x18(%rsp)
  401494:       8b 04 24                mov    (%rsp),%eax
  401497:       69 c0 3d d6 00 00       imul   $0xd63d,%eax,%eax
  40149d:       89 04 24                mov    %eax,(%rsp)
  4014a0:       8b 44 24 10             mov    0x10(%rsp),%eax
  4014a4:       69 c0 03 32 00 00       imul   $0x3203,%eax,%eax
  4014aa:       89 44 24 10             mov    %eax,0x10(%rsp)
  4014ae:       8b 44 24 10             mov    0x10(%rsp),%eax
  4014b2:       69 c0 9c ec 00 00       imul   $0xec9c,%eax,%eax
  4014b8:       89 44 24 10             mov    %eax,0x10(%rsp)
  4014bc:       8b 44 24 14             mov    0x14(%rsp),%eax
  4014c0:       69 c0 27 4e 00 00       imul   $0x4e27,%eax,%eax
  4014c6:       89 44 24 14             mov    %eax,0x14(%rsp)
  4014ca:       8b 44 24 24             mov    0x24(%rsp),%eax
  4014ce:       69 c0 0c af 00 00       imul   $0xaf0c,%eax,%eax
  4014d4:       89 44 24 24             mov    %eax,0x24(%rsp)
  4014d8:       8b 44 24 14             mov    0x14(%rsp),%eax
  4014dc:       69 c0 5e 14 00 00       imul   $0x145e,%eax,%eax
  4014e2:       89 44 24 14             mov    %eax,0x14(%rsp)
  4014e6:       8b 04 24                mov    (%rsp),%eax
  4014e9:       69 c0 71 13 00 00       imul   $0x1371,%eax,%eax
  4014ef:       89 04 24                mov    %eax,(%rsp)
  4014f2:       8b 44 24 10             mov    0x10(%rsp),%eax
  4014f6:       69 c0 a2 1f 00 00       imul   $0x1fa2,%eax,%eax
  4014fc:       89 44 24 10             mov    %eax,0x10(%rsp)
  401500:       8b 44 24 04             mov    0x4(%rsp),%eax
  401504:       69 c0 b2 77 00 00       imul   $0x77b2,%eax,%eax
  40150a:       89 44 24 04             mov    %eax,0x4(%rsp)
  40150e:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  401512:       69 c0 23 46 00 00       imul   $0x4623,%eax,%eax
  401518:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  40151c:       8b 44 24 20             mov    0x20(%rsp),%eax
  401520:       69 c0 8e 7b 00 00       imul   $0x7b8e,%eax,%eax
  401526:       89 44 24 20             mov    %eax,0x20(%rsp)
  40152a:       8b 44 24 10             mov    0x10(%rsp),%eax
  40152e:       69 c0 98 ba 00 00       imul   $0xba98,%eax,%eax
  401534:       89 44 24 10             mov    %eax,0x10(%rsp)
  401538:       8b 44 24 10             mov    0x10(%rsp),%eax
  40153c:       69 c0 c6 8a 00 00       imul   $0x8ac6,%eax,%eax
  401542:       89 44 24 10             mov    %eax,0x10(%rsp)
  401546:       8b 04 24                mov    (%rsp),%eax
  401549:       69 c0 62 df 00 00       imul   $0xdf62,%eax,%eax
  40154f:       89 04 24                mov    %eax,(%rsp)
  401552:       8b 44 24 10             mov    0x10(%rsp),%eax
  401556:       69 c0 31 6d 00 00       imul   $0x6d31,%eax,%eax
  40155c:       89 44 24 10             mov    %eax,0x10(%rsp)
  401560:       8b 44 24 10             mov    0x10(%rsp),%eax
  401564:       69 c0 4a 15 00 00       imul   $0x154a,%eax,%eax
  40156a:       89 44 24 10             mov    %eax,0x10(%rsp)
  40156e:       8b 44 24 18             mov    0x18(%rsp),%eax
  401572:       69 c0 5d 77 00 00       imul   $0x775d,%eax,%eax
  401578:       89 44 24 18             mov    %eax,0x18(%rsp)
  40157c:       8b 44 24 24             mov    0x24(%rsp),%eax
  401580:       69 c0 e5 99 00 00       imul   $0x99e5,%eax,%eax
  401586:       89 44 24 24             mov    %eax,0x24(%rsp)
  40158a:       8b 44 24 10             mov    0x10(%rsp),%eax
  40158e:       69 c0 3c 48 00 00       imul   $0x483c,%eax,%eax
  401594:       89 44 24 10             mov    %eax,0x10(%rsp)
  401598:       8b 44 24 0c             mov    0xc(%rsp),%eax
  40159c:       69 c0 bf f7 00 00       imul   $0xf7bf,%eax,%eax
  4015a2:       89 44 24 0c             mov    %eax,0xc(%rsp)
  4015a6:       8b 44 24 04             mov    0x4(%rsp),%eax
  4015aa:       69 c0 7d e4 00 00       imul   $0xe47d,%eax,%eax
  4015b0:       89 44 24 04             mov    %eax,0x4(%rsp)
  4015b4:       8b 44 24 18             mov    0x18(%rsp),%eax
  4015b8:       69 c0 1c ba 00 00       imul   $0xba1c,%eax,%eax
  4015be:       89 44 24 18             mov    %eax,0x18(%rsp)
  4015c2:       8b 04 24                mov    (%rsp),%eax
  4015c5:       69 c0 49 19 00 00       imul   $0x1949,%eax,%eax
  4015cb:       89 04 24                mov    %eax,(%rsp)
  4015ce:       8b 44 24 08             mov    0x8(%rsp),%eax
  4015d2:       69 c0 95 db 00 00       imul   $0xdb95,%eax,%eax
  4015d8:       89 44 24 08             mov    %eax,0x8(%rsp)
  4015dc:       8b 44 24 08             mov    0x8(%rsp),%eax
  4015e0:       69 c0 b9 a2 00 00       imul   $0xa2b9,%eax,%eax
  4015e6:       89 44 24 08             mov    %eax,0x8(%rsp)
  4015ea:       8b 44 24 08             mov    0x8(%rsp),%eax
  4015ee:       69 c0 f5 8f 00 00       imul   $0x8ff5,%eax,%eax
  4015f4:       89 44 24 08             mov    %eax,0x8(%rsp)
  4015f8:       8b 04 24                mov    (%rsp),%eax
  4015fb:       69 c0 86 21 00 00       imul   $0x2186,%eax,%eax
  401601:       89 04 24                mov    %eax,(%rsp)
  401604:       8b 44 24 20             mov    0x20(%rsp),%eax
  401608:       69 c0 48 6c 00 00       imul   $0x6c48,%eax,%eax
  40160e:       89 44 24 20             mov    %eax,0x20(%rsp)
  401612:       8b 04 24                mov    (%rsp),%eax
  401615:       69 c0 de 3d 00 00       imul   $0x3dde,%eax,%eax
  40161b:       89 04 24                mov    %eax,(%rsp)
  40161e:       8b 44 24 24             mov    0x24(%rsp),%eax
  401622:       69 c0 8c 7b 00 00       imul   $0x7b8c,%eax,%eax
  401628:       89 44 24 24             mov    %eax,0x24(%rsp)
  40162c:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  401630:       69 c0 30 3d 00 00       imul   $0x3d30,%eax,%eax
  401636:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  40163a:       8b 44 24 04             mov    0x4(%rsp),%eax
  40163e:       69 c0 7e ee 00 00       imul   $0xee7e,%eax,%eax
  401644:       89 44 24 04             mov    %eax,0x4(%rsp)
  401648:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  40164c:       69 c0 25 d8 00 00       imul   $0xd825,%eax,%eax
  401652:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  401656:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  40165a:       69 c0 87 18 00 00       imul   $0x1887,%eax,%eax
  401660:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  401664:       8b 04 24                mov    (%rsp),%eax
  401667:       69 c0 6f 70 00 00       imul   $0x706f,%eax,%eax
  40166d:       89 04 24                mov    %eax,(%rsp)
  401670:       8b 44 24 18             mov    0x18(%rsp),%eax
  401674:       69 c0 aa 17 00 00       imul   $0x17aa,%eax,%eax
  40167a:       89 44 24 18             mov    %eax,0x18(%rsp)
  40167e:       8b 04 24                mov    (%rsp),%eax
  401681:       69 c0 63 1c 00 00       imul   $0x1c63,%eax,%eax
  401687:       89 04 24                mov    %eax,(%rsp)
  40168a:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  40168e:       69 c0 db 4c 00 00       imul   $0x4cdb,%eax,%eax
  401694:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  401698:       8b 44 24 18             mov    0x18(%rsp),%eax
  40169c:       69 c0 84 ab 00 00       imul   $0xab84,%eax,%eax
  4016a2:       89 44 24 18             mov    %eax,0x18(%rsp)
  4016a6:       8b 44 24 10             mov    0x10(%rsp),%eax
  4016aa:       69 c0 a9 c6 00 00       imul   $0xc6a9,%eax,%eax
  4016b0:       89 44 24 10             mov    %eax,0x10(%rsp)
  4016b4:       8b 04 24                mov    (%rsp),%eax
  4016b7:       69 c0 28 4a 00 00       imul   $0x4a28,%eax,%eax
  4016bd:       89 04 24                mov    %eax,(%rsp)
  4016c0:       8b 44 24 10             mov    0x10(%rsp),%eax
  4016c4:       69 c0 86 6c 00 00       imul   $0x6c86,%eax,%eax
  4016ca:       89 44 24 10             mov    %eax,0x10(%rsp)
  4016ce:       8b 44 24 10             mov    0x10(%rsp),%eax
  4016d2:       69 c0 2c a1 00 00       imul   $0xa12c,%eax,%eax
  4016d8:       89 44 24 10             mov    %eax,0x10(%rsp)
  4016dc:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  4016e0:       69 c0 fa 17 00 00       imul   $0x17fa,%eax,%eax
  4016e6:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  4016ea:       8b 44 24 08             mov    0x8(%rsp),%eax
  4016ee:       69 c0 78 24 00 00       imul   $0x2478,%eax,%eax
  4016f4:       89 44 24 08             mov    %eax,0x8(%rsp)
  4016f8:       8b 44 24 08             mov    0x8(%rsp),%eax
  4016fc:       69 c0 1a 8a 00 00       imul   $0x8a1a,%eax,%eax
  401702:       89 44 24 08             mov    %eax,0x8(%rsp)
  401706:       8b 44 24 08             mov    0x8(%rsp),%eax
  40170a:       69 c0 5d 24 00 00       imul   $0x245d,%eax,%eax
  401710:       89 44 24 08             mov    %eax,0x8(%rsp)
  401714:       8b 44 24 18             mov    0x18(%rsp),%eax
  401718:       69 c0 36 16 00 00       imul   $0x1636,%eax,%eax
  40171e:       89 44 24 18             mov    %eax,0x18(%rsp)
  401722:       8b 44 24 24             mov    0x24(%rsp),%eax
  401726:       69 c0 fb 00 00 00       imul   $0xfb,%eax,%eax
  40172c:       89 44 24 24             mov    %eax,0x24(%rsp)
  401730:       8b 44 24 10             mov    0x10(%rsp),%eax
  401734:       69 c0 e4 1c 00 00       imul   $0x1ce4,%eax,%eax
  40173a:       89 44 24 10             mov    %eax,0x10(%rsp)
  40173e:       8b 44 24 10             mov    0x10(%rsp),%eax
  401742:       69 c0 03 3f 00 00       imul   $0x3f03,%eax,%eax
  401748:       89 44 24 10             mov    %eax,0x10(%rsp)
  40174c:       8b 44 24 08             mov    0x8(%rsp),%eax
  401750:       69 c0 57 c6 00 00       imul   $0xc657,%eax,%eax
  401756:       89 44 24 08             mov    %eax,0x8(%rsp)
  40175a:       8b 44 24 20             mov    0x20(%rsp),%eax
  40175e:       69 c0 55 06 00 00       imul   $0x655,%eax,%eax
  401764:       89 44 24 20             mov    %eax,0x20(%rsp)
  401768:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  40176c:       69 c0 13 91 00 00       imul   $0x9113,%eax,%eax
  401772:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  401776:       8b 04 24                mov    (%rsp),%eax
  401779:       69 c0 a2 3b 00 00       imul   $0x3ba2,%eax,%eax
  40177f:       89 04 24                mov    %eax,(%rsp)
  401782:       8b 44 24 18             mov    0x18(%rsp),%eax
  401786:       6b c0 17                imul   $0x17,%eax,%eax
  401789:       89 44 24 18             mov    %eax,0x18(%rsp)
  40178d:       8b 44 24 04             mov    0x4(%rsp),%eax
  401791:       69 c0 5b ae 00 00       imul   $0xae5b,%eax,%eax
  401797:       89 44 24 04             mov    %eax,0x4(%rsp)
  40179b:       8b 44 24 0c             mov    0xc(%rsp),%eax
  40179f:       69 c0 78 f1 00 00       imul   $0xf178,%eax,%eax
  4017a5:       89 44 24 0c             mov    %eax,0xc(%rsp)
  4017a9:       8b 44 24 10             mov    0x10(%rsp),%eax
  4017ad:       69 c0 6b 45 00 00       imul   $0x456b,%eax,%eax
  4017b3:       89 44 24 10             mov    %eax,0x10(%rsp)
  4017b7:       8b 44 24 14             mov    0x14(%rsp),%eax
  4017bb:       69 c0 92 2e 00 00       imul   $0x2e92,%eax,%eax
  4017c1:       89 44 24 14             mov    %eax,0x14(%rsp)
  4017c5:       8b 44 24 24             mov    0x24(%rsp),%eax
  4017c9:       69 c0 f8 9c 00 00       imul   $0x9cf8,%eax,%eax
  4017cf:       89 44 24 24             mov    %eax,0x24(%rsp)
  4017d3:       8b 04 24                mov    (%rsp),%eax
  4017d6:       69 c0 8c cb 00 00       imul   $0xcb8c,%eax,%eax
  4017dc:       89 04 24                mov    %eax,(%rsp)
  4017df:       8b 44 24 18             mov    0x18(%rsp),%eax
  4017e3:       69 c0 45 31 00 00       imul   $0x3145,%eax,%eax
  4017e9:       89 44 24 18             mov    %eax,0x18(%rsp)
  4017ed:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  4017f1:       69 c0 d8 bd 00 00       imul   $0xbdd8,%eax,%eax
  4017f7:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  4017fb:       8b 44 24 08             mov    0x8(%rsp),%eax
  4017ff:       69 c0 7f 10 00 00       imul   $0x107f,%eax,%eax
  401805:       89 44 24 08             mov    %eax,0x8(%rsp)
  401809:       8b 44 24 20             mov    0x20(%rsp),%eax
  40180d:       69 c0 ab a3 00 00       imul   $0xa3ab,%eax,%eax
  401813:       89 44 24 20             mov    %eax,0x20(%rsp)
  401817:       8b 44 24 18             mov    0x18(%rsp),%eax
  40181b:       69 c0 4b 0f 00 00       imul   $0xf4b,%eax,%eax
  401821:       89 44 24 18             mov    %eax,0x18(%rsp)
  401825:       8b 44 24 18             mov    0x18(%rsp),%eax
  401829:       69 c0 e8 aa 00 00       imul   $0xaae8,%eax,%eax
  40182f:       89 44 24 18             mov    %eax,0x18(%rsp)
  401833:       8b 44 24 10             mov    0x10(%rsp),%eax
  401837:       69 c0 34 7d 00 00       imul   $0x7d34,%eax,%eax
  40183d:       89 44 24 10             mov    %eax,0x10(%rsp)
  401841:       8b 44 24 08             mov    0x8(%rsp),%eax
  401845:       69 c0 79 c7 00 00       imul   $0xc779,%eax,%eax
  40184b:       89 44 24 08             mov    %eax,0x8(%rsp)
  40184f:       8b 44 24 24             mov    0x24(%rsp),%eax
  401853:       69 c0 b8 93 00 00       imul   $0x93b8,%eax,%eax
  401859:       89 44 24 24             mov    %eax,0x24(%rsp)
  40185d:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  401861:       69 c0 a0 3e 00 00       imul   $0x3ea0,%eax,%eax
  401867:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  40186b:       8b 44 24 08             mov    0x8(%rsp),%eax
  40186f:       69 c0 2e 34 00 00       imul   $0x342e,%eax,%eax
  401875:       89 44 24 08             mov    %eax,0x8(%rsp)
  401879:       8b 44 24 08             mov    0x8(%rsp),%eax
  40187d:       69 c0 9b 91 00 00       imul   $0x919b,%eax,%eax
  401883:       89 44 24 08             mov    %eax,0x8(%rsp)
  401887:       8b 44 24 14             mov    0x14(%rsp),%eax
  40188b:       69 c0 8a 39 00 00       imul   $0x398a,%eax,%eax
  401891:       89 44 24 14             mov    %eax,0x14(%rsp)
  401895:       8b 44 24 14             mov    0x14(%rsp),%eax
  401899:       69 c0 7d e3 00 00       imul   $0xe37d,%eax,%eax
  40189f:       89 44 24 14             mov    %eax,0x14(%rsp)
  4018a3:       8b 44 24 1c             mov    0x1c(%rsp),%eax
  4018a7:       69 c0 da 78 00 00       imul   $0x78da,%eax,%eax
  4018ad:       89 44 24 1c             mov    %eax,0x1c(%rsp)
  4018b1:       8b 44 24 08             mov    0x8(%rsp),%eax
  4018b5:       69 c0 d9 97 00 00       imul   $0x97d9,%eax,%eax
  4018bb:       89 44 24 08             mov    %eax,0x8(%rsp)
  4018bf:       8b 44 24 14             mov    0x14(%rsp),%eax
  4018c3:       69 c0 cb 90 00 00       imul   $0x90cb,%eax,%eax
  4018c9:       89 44 24 14             mov    %eax,0x14(%rsp)
  4018cd:       ba 00 00 00 00          mov    $0x0,%edx
  4018d2:       b8 00 00 00 00          mov    $0x0,%eax
  4018d7:       eb 0a                   jmp    4018e3 <scramble+0x53a>
  4018d9:       89 d1                   mov    %edx,%ecx
  4018db:       8b 0c 8c                mov    (%rsp,%rcx,4),%ecx
  4018de:       01 c8                   add    %ecx,%eax
  4018e0:       83 c2 01                add    $0x1,%edx
  4018e3:       83 fa 09                cmp    $0x9,%edx
  4018e6:       76 f1                   jbe    4018d9 <scramble+0x530>
  4018e8:       48 8b 74 24 28          mov    0x28(%rsp),%rsi
  4018ed:       64 48 33 34 25 28 00    xor    %fs:0x28,%rsi
  4018f4:       00 00
  4018f6:       74 05                   je     4018fd <scramble+0x554>
  4018f8:       e8 e3 f3 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  4018fd:       48 83 c4 38             add    $0x38,%rsp
  401901:       c3                      retq

0000000000401902 <getbuf>:
  401902:       48 83 ec 18             sub    $0x18,%rsp
  401906:       48 89 e7                mov    %rsp,%rdi
  401909:       e8 ac 02 00 00          callq  401bba <Gets>
  40190e:       b8 01 00 00 00          mov    $0x1,%eax
  401913:       48 83 c4 18             add    $0x18,%rsp
  401917:       c3                      retq

0000000000401918 <touch1>:
  401918:       48 83 ec 08             sub    $0x8,%rsp
  40191c:       48 c1 ec 04             shr    $0x4,%rsp
  401920:       48 c1 e4 04             shl    $0x4,%rsp
  401924:       c7 05 ce 3b 20 00 01    movl   $0x1,0x203bce(%rip)        # 6054fc <vlevel>
  40192b:       00 00 00
  40192e:       48 8d 3d 4f 19 00 00    lea    0x194f(%rip),%rdi        # 403284 <_IO_stdin_used+0x314>
  401935:       e8 86 f3 ff ff          callq  400cc0 <puts@plt>
  40193a:       bf 01 00 00 00          mov    $0x1,%edi
  40193f:       e8 d8 04 00 00          callq  401e1c <validate>
  401944:       bf 00 00 00 00          mov    $0x0,%edi
  401949:       e8 e2 f4 ff ff          callq  400e30 <exit@plt>

000000000040194e <touch2>:
  40194e:       48 83 ec 08             sub    $0x8,%rsp
  401952:       89 fa                   mov    %edi,%edx
  401954:       48 c1 ec 04             shr    $0x4,%rsp
  401958:       48 c1 e4 04             shl    $0x4,%rsp
  40195c:       c7 05 96 3b 20 00 02    movl   $0x2,0x203b96(%rip)        # 6054fc <vlevel>
  401963:       00 00 00
  401966:       39 3d 98 3b 20 00       cmp    %edi,0x203b98(%rip)        # 605504 <cookie>
  40196c:       75 22                   jne    401990 <touch2+0x42>
  40196e:       48 8d 35 33 19 00 00    lea    0x1933(%rip),%rsi        # 4032a8 <_IO_stdin_used+0x338>
  401975:       bf 01 00 00 00          mov    $0x1,%edi
  40197a:       b8 00 00 00 00          mov    $0x0,%eax
  40197f:       e8 5c f4 ff ff          callq  400de0 <__printf_chk@plt>
  401984:       bf 02 00 00 00          mov    $0x2,%edi
  401989:       e8 8e 04 00 00          callq  401e1c <validate>
  40198e:       eb 20                   jmp    4019b0 <touch2+0x62>
  401990:       48 8d 35 39 19 00 00    lea    0x1939(%rip),%rsi        # 4032d0 <_IO_stdin_used+0x360>
  401997:       bf 01 00 00 00          mov    $0x1,%edi
  40199c:       b8 00 00 00 00          mov    $0x0,%eax
  4019a1:       e8 3a f4 ff ff          callq  400de0 <__printf_chk@plt>
  4019a6:       bf 02 00 00 00          mov    $0x2,%edi
  4019ab:       e8 39 05 00 00          callq  401ee9 <fail>
  4019b0:       bf 00 00 00 00          mov    $0x0,%edi
  4019b5:       e8 76 f4 ff ff          callq  400e30 <exit@plt>

00000000004019ba <hexmatch>:
  4019ba:       41 54                   push   %r12
  4019bc:       55                      push   %rbp
  4019bd:       53                      push   %rbx
  4019be:       48 83 c4 80             add    $0xffffffffffffff80,%rsp
  4019c2:       89 fd                   mov    %edi,%ebp
  4019c4:       48 89 f3                mov    %rsi,%rbx
  4019c7:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4019ce:       00 00
  4019d0:       48 89 44 24 78          mov    %rax,0x78(%rsp)
  4019d5:       31 c0                   xor    %eax,%eax
  4019d7:       e8 c4 f3 ff ff          callq  400da0 <random@plt>
  4019dc:       48 89 c1                mov    %rax,%rcx
  4019df:       48 ba 0b d7 a3 70 3d    movabs $0xa3d70a3d70a3d70b,%rdx
  4019e6:       0a d7 a3
  4019e9:       48 f7 ea                imul   %rdx
  4019ec:       48 01 ca                add    %rcx,%rdx
  4019ef:       48 c1 fa 06             sar    $0x6,%rdx
  4019f3:       48 89 c8                mov    %rcx,%rax
  4019f6:       48 c1 f8 3f             sar    $0x3f,%rax
  4019fa:       48 29 c2                sub    %rax,%rdx
  4019fd:       48 8d 04 92             lea    (%rdx,%rdx,4),%rax
  401a01:       48 8d 14 80             lea    (%rax,%rax,4),%rdx
  401a05:       48 8d 04 95 00 00 00    lea    0x0(,%rdx,4),%rax
  401a0c:       00
  401a0d:       48 29 c1                sub    %rax,%rcx
  401a10:       4c 8d 24 0c             lea    (%rsp,%rcx,1),%r12
  401a14:       41 89 e8                mov    %ebp,%r8d
  401a17:       48 8d 0d 83 18 00 00    lea    0x1883(%rip),%rcx        # 4032a1 <_IO_stdin_used+0x331>
  401a1e:       48 c7 c2 ff ff ff ff    mov    $0xffffffffffffffff,%rdx
  401a25:       be 01 00 00 00          mov    $0x1,%esi
  401a2a:       4c 89 e7                mov    %r12,%rdi
  401a2d:       b8 00 00 00 00          mov    $0x0,%eax
  401a32:       e8 29 f4 ff ff          callq  400e60 <__sprintf_chk@plt>
  401a37:       ba 09 00 00 00          mov    $0x9,%edx
  401a3c:       4c 89 e6                mov    %r12,%rsi
  401a3f:       48 89 df                mov    %rbx,%rdi
  401a42:       e8 59 f2 ff ff          callq  400ca0 <strncmp@plt>
  401a47:       85 c0                   test   %eax,%eax
  401a49:       0f 94 c0                sete   %al
  401a4c:       48 8b 5c 24 78          mov    0x78(%rsp),%rbx
  401a51:       64 48 33 1c 25 28 00    xor    %fs:0x28,%rbx
  401a58:       00 00
  401a5a:       74 05                   je     401a61 <hexmatch+0xa7>
  401a5c:       e8 7f f2 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  401a61:       0f b6 c0                movzbl %al,%eax
  401a64:       48 83 ec 80             sub    $0xffffffffffffff80,%rsp
  401a68:       5b                      pop    %rbx
  401a69:       5d                      pop    %rbp
  401a6a:       41 5c                   pop    %r12
  401a6c:       c3                      retq

0000000000401a6d <touch3>:
  401a6d:       53                      push   %rbx
  401a6e:       48 89 fb                mov    %rdi,%rbx
  401a71:       48 c1 ec 04             shr    $0x4,%rsp
  401a75:       48 c1 e4 04             shl    $0x4,%rsp
  401a79:       c7 05 79 3a 20 00 03    movl   $0x3,0x203a79(%rip)        # 6054fc <vlevel>
  401a80:       00 00 00
  401a83:       48 89 fe                mov    %rdi,%rsi
  401a86:       8b 3d 78 3a 20 00       mov    0x203a78(%rip),%edi        # 605504 <cookie>
  401a8c:       e8 29 ff ff ff          callq  4019ba <hexmatch>
  401a91:       85 c0                   test   %eax,%eax
  401a93:       74 25                   je     401aba <touch3+0x4d>
  401a95:       48 89 da                mov    %rbx,%rdx
  401a98:       48 8d 35 59 18 00 00    lea    0x1859(%rip),%rsi        # 4032f8 <_IO_stdin_used+0x388>
  401a9f:       bf 01 00 00 00          mov    $0x1,%edi
  401aa4:       b8 00 00 00 00          mov    $0x0,%eax
  401aa9:       e8 32 f3 ff ff          callq  400de0 <__printf_chk@plt>
  401aae:       bf 03 00 00 00          mov    $0x3,%edi
  401ab3:       e8 64 03 00 00          callq  401e1c <validate>
  401ab8:       eb 23                   jmp    401add <touch3+0x70>
  401aba:       48 89 da                mov    %rbx,%rdx
  401abd:       48 8d 35 5c 18 00 00    lea    0x185c(%rip),%rsi        # 403320 <_IO_stdin_used+0x3b0>
  401ac4:       bf 01 00 00 00          mov    $0x1,%edi
  401ac9:       b8 00 00 00 00          mov    $0x0,%eax
  401ace:       e8 0d f3 ff ff          callq  400de0 <__printf_chk@plt>
  401ad3:       bf 03 00 00 00          mov    $0x3,%edi
  401ad8:       e8 0c 04 00 00          callq  401ee9 <fail>
  401add:       bf 00 00 00 00          mov    $0x0,%edi
  401ae2:       e8 49 f3 ff ff          callq  400e30 <exit@plt>

0000000000401ae7 <test>:
  401ae7:       48 83 ec 08             sub    $0x8,%rsp
  401aeb:       b8 00 00 00 00          mov    $0x0,%eax
  401af0:       e8 0d fe ff ff          callq  401902 <getbuf>
  401af5:       89 c2                   mov    %eax,%edx
  401af7:       48 8d 35 4a 18 00 00    lea    0x184a(%rip),%rsi        # 403348 <_IO_stdin_used+0x3d8>
  401afe:       bf 01 00 00 00          mov    $0x1,%edi
  401b03:       b8 00 00 00 00          mov    $0x0,%eax
  401b08:       e8 d3 f2 ff ff          callq  400de0 <__printf_chk@plt>
  401b0d:       48 83 c4 08             add    $0x8,%rsp
  401b11:       c3                      retq

0000000000401b12 <save_char>:
  401b12:       8b 05 0c 46 20 00       mov    0x20460c(%rip),%eax        # 606124 <gets_cnt>
  401b18:       3d ff 03 00 00          cmp    $0x3ff,%eax
  401b1d:       7f 4a                   jg     401b69 <save_char+0x57>
  401b1f:       8d 14 40                lea    (%rax,%rax,2),%edx
  401b22:       89 f9                   mov    %edi,%ecx
  401b24:       c0 e9 04                shr    $0x4,%cl
  401b27:       4c 8d 05 42 1b 00 00    lea    0x1b42(%rip),%r8        # 403670 <trans_char>
  401b2e:       83 e1 0f                and    $0xf,%ecx
  401b31:       45 0f b6 0c 08          movzbl (%r8,%rcx,1),%r9d
  401b36:       48 8d 0d e3 39 20 00    lea    0x2039e3(%rip),%rcx        # 605520 <gets_buf>
  401b3d:       48 63 f2                movslq %edx,%rsi
  401b40:       44 88 0c 31             mov    %r9b,(%rcx,%rsi,1)
  401b44:       8d 72 01                lea    0x1(%rdx),%esi
  401b47:       83 e7 0f                and    $0xf,%edi
  401b4a:       41 0f b6 3c 38          movzbl (%r8,%rdi,1),%edi
  401b4f:       48 63 f6                movslq %esi,%rsi
  401b52:       40 88 3c 31             mov    %dil,(%rcx,%rsi,1)
  401b56:       83 c2 02                add    $0x2,%edx
  401b59:       48 63 d2                movslq %edx,%rdx
  401b5c:       c6 04 11 20             movb   $0x20,(%rcx,%rdx,1)
  401b60:       83 c0 01                add    $0x1,%eax
  401b63:       89 05 bb 45 20 00       mov    %eax,0x2045bb(%rip)        # 606124 <gets_cnt>
  401b69:       f3 c3                   repz retq

0000000000401b6b <save_term>:
  401b6b:       8b 05 b3 45 20 00       mov    0x2045b3(%rip),%eax        # 606124 <gets_cnt>
  401b71:       8d 04 40                lea    (%rax,%rax,2),%eax
  401b74:       48 98                   cltq
  401b76:       48 8d 15 a3 39 20 00    lea    0x2039a3(%rip),%rdx        # 605520 <gets_buf>
  401b7d:       c6 04 02 00             movb   $0x0,(%rdx,%rax,1)
  401b81:       c3                      retq

0000000000401b82 <check_fail>:
  401b82:       48 83 ec 08             sub    $0x8,%rsp
  401b86:       0f be 15 9b 45 20 00    movsbl 0x20459b(%rip),%edx        # 606128 <target_prefix>
  401b8d:       4c 8d 05 8c 39 20 00    lea    0x20398c(%rip),%r8        # 605520 <gets_buf>
  401b94:       8b 0d 5e 39 20 00       mov    0x20395e(%rip),%ecx        # 6054f8 <check_level>
  401b9a:       48 8d 35 ca 17 00 00    lea    0x17ca(%rip),%rsi        # 40336b <_IO_stdin_used+0x3fb>
  401ba1:       bf 01 00 00 00          mov    $0x1,%edi
  401ba6:       b8 00 00 00 00          mov    $0x0,%eax
  401bab:       e8 30 f2 ff ff          callq  400de0 <__printf_chk@plt>
  401bb0:       bf 01 00 00 00          mov    $0x1,%edi
  401bb5:       e8 76 f2 ff ff          callq  400e30 <exit@plt>

0000000000401bba <Gets>:
  401bba:       41 54                   push   %r12
  401bbc:       55                      push   %rbp
  401bbd:       53                      push   %rbx
  401bbe:       49 89 fc                mov    %rdi,%r12
  401bc1:       c7 05 59 45 20 00 00    movl   $0x0,0x204559(%rip)        # 606124 <gets_cnt>
  401bc8:       00 00 00
  401bcb:       48 89 fb                mov    %rdi,%rbx
  401bce:       eb 11                   jmp    401be1 <Gets+0x27>
  401bd0:       48 8d 6b 01             lea    0x1(%rbx),%rbp
  401bd4:       88 03                   mov    %al,(%rbx)
  401bd6:       0f b6 f8                movzbl %al,%edi
  401bd9:       e8 34 ff ff ff          callq  401b12 <save_char>
  401bde:       48 89 eb                mov    %rbp,%rbx
  401be1:       48 8b 3d 08 39 20 00    mov    0x203908(%rip),%rdi        # 6054f0 <infile>
  401be8:       e8 c3 f1 ff ff          callq  400db0 <_IO_getc@plt>
  401bed:       83 f8 ff                cmp    $0xffffffff,%eax
  401bf0:       74 05                   je     401bf7 <Gets+0x3d>
  401bf2:       83 f8 0a                cmp    $0xa,%eax
  401bf5:       75 d9                   jne    401bd0 <Gets+0x16>
  401bf7:       c6 03 00                movb   $0x0,(%rbx)
  401bfa:       b8 00 00 00 00          mov    $0x0,%eax
  401bff:       e8 67 ff ff ff          callq  401b6b <save_term>
  401c04:       4c 89 e0                mov    %r12,%rax
  401c07:       5b                      pop    %rbx
  401c08:       5d                      pop    %rbp
  401c09:       41 5c                   pop    %r12
  401c0b:       c3                      retq

0000000000401c0c <notify_server>:
  401c0c:       53                      push   %rbx
  401c0d:       48 81 ec 10 40 00 00    sub    $0x4010,%rsp
  401c14:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  401c1b:       00 00
  401c1d:       48 89 84 24 08 40 00    mov    %rax,0x4008(%rsp)
  401c24:       00
  401c25:       31 c0                   xor    %eax,%eax
  401c27:       83 3d da 38 20 00 00    cmpl   $0x0,0x2038da(%rip)        # 605508 <is_checker>
  401c2e:       0f 85 c7 01 00 00       jne    401dfb <notify_server+0x1ef>
  401c34:       89 fb                   mov    %edi,%ebx
  401c36:       8b 05 e8 44 20 00       mov    0x2044e8(%rip),%eax        # 606124 <gets_cnt>
  401c3c:       83 c0 64                add    $0x64,%eax
  401c3f:       3d 00 20 00 00          cmp    $0x2000,%eax
  401c44:       7e 20                   jle    401c66 <notify_server+0x5a>
  401c46:       48 8d 35 53 18 00 00    lea    0x1853(%rip),%rsi        # 4034a0 <_IO_stdin_used+0x530>
  401c4d:       bf 01 00 00 00          mov    $0x1,%edi
  401c52:       b8 00 00 00 00          mov    $0x0,%eax
  401c57:       e8 84 f1 ff ff          callq  400de0 <__printf_chk@plt>
  401c5c:       bf 01 00 00 00          mov    $0x1,%edi
  401c61:       e8 ca f1 ff ff          callq  400e30 <exit@plt>
  401c66:       0f be 05 bb 44 20 00    movsbl 0x2044bb(%rip),%eax        # 606128 <target_prefix>
  401c6d:       83 3d 14 38 20 00 00    cmpl   $0x0,0x203814(%rip)        # 605488 <notify>
  401c74:       74 08                   je     401c7e <notify_server+0x72>
  401c76:       8b 15 84 38 20 00       mov    0x203884(%rip),%edx        # 605500 <authkey>
  401c7c:       eb 05                   jmp    401c83 <notify_server+0x77>
  401c7e:       ba ff ff ff ff          mov    $0xffffffff,%edx
  401c83:       85 db                   test   %ebx,%ebx
  401c85:       74 09                   je     401c90 <notify_server+0x84>
  401c87:       4c 8d 0d f3 16 00 00    lea    0x16f3(%rip),%r9        # 403381 <_IO_stdin_used+0x411>
  401c8e:       eb 07                   jmp    401c97 <notify_server+0x8b>
  401c90:       4c 8d 0d ef 16 00 00    lea    0x16ef(%rip),%r9        # 403386 <_IO_stdin_used+0x416>
  401c97:       48 89 e7                mov    %rsp,%rdi
  401c9a:       48 8d 0d 7f 38 20 00    lea    0x20387f(%rip),%rcx        # 605520 <gets_buf>
  401ca1:       51                      push   %rcx
  401ca2:       56                      push   %rsi
  401ca3:       50                      push   %rax
  401ca4:       52                      push   %rdx
  401ca5:       44 8b 05 84 34 20 00    mov    0x203484(%rip),%r8d        # 605130 <target_id>
  401cac:       48 8d 0d d8 16 00 00    lea    0x16d8(%rip),%rcx        # 40338b <_IO_stdin_used+0x41b>
  401cb3:       ba 00 20 00 00          mov    $0x2000,%edx
  401cb8:       be 01 00 00 00          mov    $0x1,%esi
  401cbd:       b8 00 00 00 00          mov    $0x0,%eax
  401cc2:       e8 99 f1 ff ff          callq  400e60 <__sprintf_chk@plt>
  401cc7:       48 83 c4 20             add    $0x20,%rsp
  401ccb:       83 3d b6 37 20 00 00    cmpl   $0x0,0x2037b6(%rip)        # 605488 <notify>
  401cd2:       0f 84 89 00 00 00       je     401d61 <notify_server+0x155>
  401cd8:       85 db                   test   %ebx,%ebx
  401cda:       74 74                   je     401d50 <notify_server+0x144>
  401cdc:       48 89 e1                mov    %rsp,%rcx
  401cdf:       4c 8d 8c 24 00 20 00    lea    0x2000(%rsp),%r9
  401ce6:       00
  401ce7:       41 b8 00 00 00 00       mov    $0x0,%r8d
  401ced:       48 8b 15 54 34 20 00    mov    0x203454(%rip),%rdx        # 605148 <lab>
  401cf4:       48 8b 35 55 34 20 00    mov    0x203455(%rip),%rsi        # 605150 <course>
  401cfb:       48 8b 3d 3e 34 20 00    mov    0x20343e(%rip),%rdi        # 605140 <user_id>
  401d02:       e8 1c 11 00 00          callq  402e23 <driver_post>
  401d07:       85 c0                   test   %eax,%eax
  401d09:       79 28                   jns    401d33 <notify_server+0x127>
  401d0b:       48 8d 94 24 00 20 00    lea    0x2000(%rsp),%rdx
  401d12:       00
  401d13:       48 8d 35 8d 16 00 00    lea    0x168d(%rip),%rsi        # 4033a7 <_IO_stdin_used+0x437>
  401d1a:       bf 01 00 00 00          mov    $0x1,%edi
  401d1f:       b8 00 00 00 00          mov    $0x0,%eax
  401d24:       e8 b7 f0 ff ff          callq  400de0 <__printf_chk@plt>
  401d29:       bf 01 00 00 00          mov    $0x1,%edi
  401d2e:       e8 fd f0 ff ff          callq  400e30 <exit@plt>
  401d33:       48 8d 3d 96 17 00 00    lea    0x1796(%rip),%rdi        # 4034d0 <_IO_stdin_used+0x560>
  401d3a:       e8 81 ef ff ff          callq  400cc0 <puts@plt>
  401d3f:       48 8d 3d 6d 16 00 00    lea    0x166d(%rip),%rdi        # 4033b3 <_IO_stdin_used+0x443>
  401d46:       e8 75 ef ff ff          callq  400cc0 <puts@plt>
  401d4b:       e9 ab 00 00 00          jmpq   401dfb <notify_server+0x1ef>
  401d50:       48 8d 3d 66 16 00 00    lea    0x1666(%rip),%rdi        # 4033bd <_IO_stdin_used+0x44d>
  401d57:       e8 64 ef ff ff          callq  400cc0 <puts@plt>
  401d5c:       e9 9a 00 00 00          jmpq   401dfb <notify_server+0x1ef>
  401d61:       85 db                   test   %ebx,%ebx
  401d63:       74 09                   je     401d6e <notify_server+0x162>
  401d65:       48 8d 15 15 16 00 00    lea    0x1615(%rip),%rdx        # 403381 <_IO_stdin_used+0x411>
  401d6c:       eb 07                   jmp    401d75 <notify_server+0x169>
  401d6e:       48 8d 15 11 16 00 00    lea    0x1611(%rip),%rdx        # 403386 <_IO_stdin_used+0x416>
  401d75:       48 8d 35 8c 17 00 00    lea    0x178c(%rip),%rsi        # 403508 <_IO_stdin_used+0x598>
  401d7c:       bf 01 00 00 00          mov    $0x1,%edi
  401d81:       b8 00 00 00 00          mov    $0x0,%eax
  401d86:       e8 55 f0 ff ff          callq  400de0 <__printf_chk@plt>
  401d8b:       48 8b 15 ae 33 20 00    mov    0x2033ae(%rip),%rdx        # 605140 <user_id>
  401d92:       48 8d 35 2b 16 00 00    lea    0x162b(%rip),%rsi        # 4033c4 <_IO_stdin_used+0x454>
  401d99:       bf 01 00 00 00          mov    $0x1,%edi
  401d9e:       b8 00 00 00 00          mov    $0x0,%eax
  401da3:       e8 38 f0 ff ff          callq  400de0 <__printf_chk@plt>
  401da8:       48 8b 15 a1 33 20 00    mov    0x2033a1(%rip),%rdx        # 605150 <course>
  401daf:       48 8d 35 1b 16 00 00    lea    0x161b(%rip),%rsi        # 4033d1 <_IO_stdin_used+0x461>
  401db6:       bf 01 00 00 00          mov    $0x1,%edi
  401dbb:       b8 00 00 00 00          mov    $0x0,%eax
  401dc0:       e8 1b f0 ff ff          callq  400de0 <__printf_chk@plt>
  401dc5:       48 8b 15 7c 33 20 00    mov    0x20337c(%rip),%rdx        # 605148 <lab>
  401dcc:       48 8d 35 0a 16 00 00    lea    0x160a(%rip),%rsi        # 4033dd <_IO_stdin_used+0x46d>
  401dd3:       bf 01 00 00 00          mov    $0x1,%edi
  401dd8:       b8 00 00 00 00          mov    $0x0,%eax
  401ddd:       e8 fe ef ff ff          callq  400de0 <__printf_chk@plt>
  401de2:       48 89 e2                mov    %rsp,%rdx
  401de5:       48 8d 35 fa 15 00 00    lea    0x15fa(%rip),%rsi        # 4033e6 <_IO_stdin_used+0x476>
  401dec:       bf 01 00 00 00          mov    $0x1,%edi
  401df1:       b8 00 00 00 00          mov    $0x0,%eax
  401df6:       e8 e5 ef ff ff          callq  400de0 <__printf_chk@plt>
  401dfb:       48 8b 84 24 08 40 00    mov    0x4008(%rsp),%rax
  401e02:       00
  401e03:       64 48 33 04 25 28 00    xor    %fs:0x28,%rax
  401e0a:       00 00
  401e0c:       74 05                   je     401e13 <notify_server+0x207>
  401e0e:       e8 cd ee ff ff          callq  400ce0 <__stack_chk_fail@plt>
  401e13:       48 81 c4 10 40 00 00    add    $0x4010,%rsp
  401e1a:       5b                      pop    %rbx
  401e1b:       c3                      retq

0000000000401e1c <validate>:
  401e1c:       53                      push   %rbx
  401e1d:       89 fb                   mov    %edi,%ebx
  401e1f:       83 3d e2 36 20 00 00    cmpl   $0x0,0x2036e2(%rip)        # 605508 <is_checker>
  401e26:       74 72                   je     401e9a <validate+0x7e>
  401e28:       39 3d ce 36 20 00       cmp    %edi,0x2036ce(%rip)        # 6054fc <vlevel>
  401e2e:       74 16                   je     401e46 <validate+0x2a>
  401e30:       48 8d 3d bb 15 00 00    lea    0x15bb(%rip),%rdi        # 4033f2 <_IO_stdin_used+0x482>
  401e37:       e8 84 ee ff ff          callq  400cc0 <puts@plt>
  401e3c:       b8 00 00 00 00          mov    $0x0,%eax
  401e41:       e8 3c fd ff ff          callq  401b82 <check_fail>
  401e46:       8b 15 ac 36 20 00       mov    0x2036ac(%rip),%edx        # 6054f8 <check_level>
  401e4c:       39 d7                   cmp    %edx,%edi
  401e4e:       74 22                   je     401e72 <validate+0x56>
  401e50:       89 f9                   mov    %edi,%ecx
  401e52:       48 8d 35 d7 16 00 00    lea    0x16d7(%rip),%rsi        # 403530 <_IO_stdin_used+0x5c0>
  401e59:       bf 01 00 00 00          mov    $0x1,%edi
  401e5e:       b8 00 00 00 00          mov    $0x0,%eax
  401e63:       e8 78 ef ff ff          callq  400de0 <__printf_chk@plt>
  401e68:       b8 00 00 00 00          mov    $0x0,%eax
  401e6d:       e8 10 fd ff ff          callq  401b82 <check_fail>
  401e72:       0f be 15 af 42 20 00    movsbl 0x2042af(%rip),%edx        # 606128 <target_prefix>
  401e79:       4c 8d 05 a0 36 20 00    lea    0x2036a0(%rip),%r8        # 605520 <gets_buf>
  401e80:       89 f9                   mov    %edi,%ecx
  401e82:       48 8d 35 87 15 00 00    lea    0x1587(%rip),%rsi        # 403410 <_IO_stdin_used+0x4a0>
  401e89:       bf 01 00 00 00          mov    $0x1,%edi
  401e8e:       b8 00 00 00 00          mov    $0x0,%eax
  401e93:       e8 48 ef ff ff          callq  400de0 <__printf_chk@plt>
  401e98:       eb 4d                   jmp    401ee7 <validate+0xcb>
  401e9a:       3b 3d 5c 36 20 00       cmp    0x20365c(%rip),%edi        # 6054fc <vlevel>
  401ea0:       74 1a                   je     401ebc <validate+0xa0>
  401ea2:       48 8d 3d 49 15 00 00    lea    0x1549(%rip),%rdi        # 4033f2 <_IO_stdin_used+0x482>
  401ea9:       e8 12 ee ff ff          callq  400cc0 <puts@plt>
  401eae:       89 de                   mov    %ebx,%esi
  401eb0:       bf 00 00 00 00          mov    $0x0,%edi
  401eb5:       e8 52 fd ff ff          callq  401c0c <notify_server>
  401eba:       eb 2b                   jmp    401ee7 <validate+0xcb>
  401ebc:       0f be 0d 65 42 20 00    movsbl 0x204265(%rip),%ecx        # 606128 <target_prefix>
  401ec3:       89 fa                   mov    %edi,%edx
  401ec5:       48 8d 35 8c 16 00 00    lea    0x168c(%rip),%rsi        # 403558 <_IO_stdin_used+0x5e8>
  401ecc:       bf 01 00 00 00          mov    $0x1,%edi
  401ed1:       b8 00 00 00 00          mov    $0x0,%eax
  401ed6:       e8 05 ef ff ff          callq  400de0 <__printf_chk@plt>
  401edb:       89 de                   mov    %ebx,%esi
  401edd:       bf 01 00 00 00          mov    $0x1,%edi
  401ee2:       e8 25 fd ff ff          callq  401c0c <notify_server>
  401ee7:       5b                      pop    %rbx
  401ee8:       c3                      retq

0000000000401ee9 <fail>:
  401ee9:       48 83 ec 08             sub    $0x8,%rsp
  401eed:       83 3d 14 36 20 00 00    cmpl   $0x0,0x203614(%rip)        # 605508 <is_checker>
  401ef4:       74 0a                   je     401f00 <fail+0x17>
  401ef6:       b8 00 00 00 00          mov    $0x0,%eax
  401efb:       e8 82 fc ff ff          callq  401b82 <check_fail>
  401f00:       89 fe                   mov    %edi,%esi
  401f02:       bf 00 00 00 00          mov    $0x0,%edi
  401f07:       e8 00 fd ff ff          callq  401c0c <notify_server>
  401f0c:       48 83 c4 08             add    $0x8,%rsp
  401f10:       c3                      retq

0000000000401f11 <bushandler>:
  401f11:       48 83 ec 08             sub    $0x8,%rsp
  401f15:       83 3d ec 35 20 00 00    cmpl   $0x0,0x2035ec(%rip)        # 605508 <is_checker>
  401f1c:       74 16                   je     401f34 <bushandler+0x23>
  401f1e:       48 8d 3d 00 15 00 00    lea    0x1500(%rip),%rdi        # 403425 <_IO_stdin_used+0x4b5>
  401f25:       e8 96 ed ff ff          callq  400cc0 <puts@plt>
  401f2a:       b8 00 00 00 00          mov    $0x0,%eax
  401f2f:       e8 4e fc ff ff          callq  401b82 <check_fail>
  401f34:       48 8d 3d 55 16 00 00    lea    0x1655(%rip),%rdi        # 403590 <_IO_stdin_used+0x620>
  401f3b:       e8 80 ed ff ff          callq  400cc0 <puts@plt>
  401f40:       48 8d 3d e8 14 00 00    lea    0x14e8(%rip),%rdi        # 40342f <_IO_stdin_used+0x4bf>
  401f47:       e8 74 ed ff ff          callq  400cc0 <puts@plt>
  401f4c:       be 00 00 00 00          mov    $0x0,%esi
  401f51:       bf 00 00 00 00          mov    $0x0,%edi
  401f56:       e8 b1 fc ff ff          callq  401c0c <notify_server>
  401f5b:       bf 01 00 00 00          mov    $0x1,%edi
  401f60:       e8 cb ee ff ff          callq  400e30 <exit@plt>

0000000000401f65 <seghandler>:
  401f65:       48 83 ec 08             sub    $0x8,%rsp
  401f69:       83 3d 98 35 20 00 00    cmpl   $0x0,0x203598(%rip)        # 605508 <is_checker>
  401f70:       74 16                   je     401f88 <seghandler+0x23>
  401f72:       48 8d 3d cc 14 00 00    lea    0x14cc(%rip),%rdi        # 403445 <_IO_stdin_used+0x4d5>
  401f79:       e8 42 ed ff ff          callq  400cc0 <puts@plt>
  401f7e:       b8 00 00 00 00          mov    $0x0,%eax
  401f83:       e8 fa fb ff ff          callq  401b82 <check_fail>
  401f88:       48 8d 3d 21 16 00 00    lea    0x1621(%rip),%rdi        # 4035b0 <_IO_stdin_used+0x640>
  401f8f:       e8 2c ed ff ff          callq  400cc0 <puts@plt>
  401f94:       48 8d 3d 94 14 00 00    lea    0x1494(%rip),%rdi        # 40342f <_IO_stdin_used+0x4bf>
  401f9b:       e8 20 ed ff ff          callq  400cc0 <puts@plt>
  401fa0:       be 00 00 00 00          mov    $0x0,%esi
  401fa5:       bf 00 00 00 00          mov    $0x0,%edi
  401faa:       e8 5d fc ff ff          callq  401c0c <notify_server>
  401faf:       bf 01 00 00 00          mov    $0x1,%edi
  401fb4:       e8 77 ee ff ff          callq  400e30 <exit@plt>

0000000000401fb9 <illegalhandler>:
  401fb9:       48 83 ec 08             sub    $0x8,%rsp
  401fbd:       83 3d 44 35 20 00 00    cmpl   $0x0,0x203544(%rip)        # 605508 <is_checker>
  401fc4:       74 16                   je     401fdc <illegalhandler+0x23>
  401fc6:       48 8d 3d 8b 14 00 00    lea    0x148b(%rip),%rdi        # 403458 <_IO_stdin_used+0x4e8>
  401fcd:       e8 ee ec ff ff          callq  400cc0 <puts@plt>
  401fd2:       b8 00 00 00 00          mov    $0x0,%eax
  401fd7:       e8 a6 fb ff ff          callq  401b82 <check_fail>
  401fdc:       48 8d 3d f5 15 00 00    lea    0x15f5(%rip),%rdi        # 4035d8 <_IO_stdin_used+0x668>
  401fe3:       e8 d8 ec ff ff          callq  400cc0 <puts@plt>
  401fe8:       48 8d 3d 40 14 00 00    lea    0x1440(%rip),%rdi        # 40342f <_IO_stdin_used+0x4bf>
  401fef:       e8 cc ec ff ff          callq  400cc0 <puts@plt>
  401ff4:       be 00 00 00 00          mov    $0x0,%esi
  401ff9:       bf 00 00 00 00          mov    $0x0,%edi
  401ffe:       e8 09 fc ff ff          callq  401c0c <notify_server>
  402003:       bf 01 00 00 00          mov    $0x1,%edi
  402008:       e8 23 ee ff ff          callq  400e30 <exit@plt>

000000000040200d <sigalrmhandler>:
  40200d:       48 83 ec 08             sub    $0x8,%rsp
  402011:       83 3d f0 34 20 00 00    cmpl   $0x0,0x2034f0(%rip)        # 605508 <is_checker>
  402018:       74 16                   je     402030 <sigalrmhandler+0x23>
  40201a:       48 8d 3d 4b 14 00 00    lea    0x144b(%rip),%rdi        # 40346c <_IO_stdin_used+0x4fc>
  402021:       e8 9a ec ff ff          callq  400cc0 <puts@plt>
  402026:       b8 00 00 00 00          mov    $0x0,%eax
  40202b:       e8 52 fb ff ff          callq  401b82 <check_fail>
  402030:       ba 05 00 00 00          mov    $0x5,%edx
  402035:       48 8d 35 cc 15 00 00    lea    0x15cc(%rip),%rsi        # 403608 <_IO_stdin_used+0x698>
  40203c:       bf 01 00 00 00          mov    $0x1,%edi
  402041:       b8 00 00 00 00          mov    $0x0,%eax
  402046:       e8 95 ed ff ff          callq  400de0 <__printf_chk@plt>
  40204b:       be 00 00 00 00          mov    $0x0,%esi
  402050:       bf 00 00 00 00          mov    $0x0,%edi
  402055:       e8 b2 fb ff ff          callq  401c0c <notify_server>
  40205a:       bf 01 00 00 00          mov    $0x1,%edi
  40205f:       e8 cc ed ff ff          callq  400e30 <exit@plt>

0000000000402064 <launch>:
  402064:       55                      push   %rbp
  402065:       48 89 e5                mov    %rsp,%rbp
  402068:       48 83 ec 10             sub    $0x10,%rsp
  40206c:       48 89 fa                mov    %rdi,%rdx
  40206f:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  402076:       00 00
  402078:       48 89 45 f8             mov    %rax,-0x8(%rbp)
  40207c:       31 c0                   xor    %eax,%eax
  40207e:       48 8d 47 1e             lea    0x1e(%rdi),%rax
  402082:       48 83 e0 f0             and    $0xfffffffffffffff0,%rax
  402086:       48 29 c4                sub    %rax,%rsp
  402089:       48 8d 7c 24 0f          lea    0xf(%rsp),%rdi
  40208e:       48 83 e7 f0             and    $0xfffffffffffffff0,%rdi
  402092:       be f4 00 00 00          mov    $0xf4,%esi
  402097:       e8 64 ec ff ff          callq  400d00 <memset@plt>
  40209c:       48 8b 05 fd 33 20 00    mov    0x2033fd(%rip),%rax        # 6054a0 <stdin@@GLIBC_2.2.5>
  4020a3:       48 39 05 46 34 20 00    cmp    %rax,0x203446(%rip)        # 6054f0 <infile>
  4020aa:       75 16                   jne    4020c2 <launch+0x5e>
  4020ac:       48 8d 35 c1 13 00 00    lea    0x13c1(%rip),%rsi        # 403474 <_IO_stdin_used+0x504>
  4020b3:       bf 01 00 00 00          mov    $0x1,%edi
  4020b8:       b8 00 00 00 00          mov    $0x0,%eax
  4020bd:       e8 1e ed ff ff          callq  400de0 <__printf_chk@plt>
  4020c2:       c7 05 30 34 20 00 00    movl   $0x0,0x203430(%rip)        # 6054fc <vlevel>
  4020c9:       00 00 00
  4020cc:       b8 00 00 00 00          mov    $0x0,%eax
  4020d1:       e8 11 fa ff ff          callq  401ae7 <test>
  4020d6:       83 3d 2b 34 20 00 00    cmpl   $0x0,0x20342b(%rip)        # 605508 <is_checker>
  4020dd:       74 16                   je     4020f5 <launch+0x91>
  4020df:       48 8d 3d 9b 13 00 00    lea    0x139b(%rip),%rdi        # 403481 <_IO_stdin_used+0x511>
  4020e6:       e8 d5 eb ff ff          callq  400cc0 <puts@plt>
  4020eb:       b8 00 00 00 00          mov    $0x0,%eax
  4020f0:       e8 8d fa ff ff          callq  401b82 <check_fail>
  4020f5:       48 8d 3d 90 13 00 00    lea    0x1390(%rip),%rdi        # 40348c <_IO_stdin_used+0x51c>
  4020fc:       e8 bf eb ff ff          callq  400cc0 <puts@plt>
  402101:       48 8b 45 f8             mov    -0x8(%rbp),%rax
  402105:       64 48 33 04 25 28 00    xor    %fs:0x28,%rax
  40210c:       00 00
  40210e:       74 05                   je     402115 <launch+0xb1>
  402110:       e8 cb eb ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402115:       c9                      leaveq
  402116:       c3                      retq

0000000000402117 <stable_launch>:
  402117:       53                      push   %rbx
  402118:       48 89 3d c9 33 20 00    mov    %rdi,0x2033c9(%rip)        # 6054e8 <global_offset>
  40211f:       41 b9 00 00 00 00       mov    $0x0,%r9d
  402125:       41 b8 00 00 00 00       mov    $0x0,%r8d
  40212b:       b9 32 01 00 00          mov    $0x132,%ecx
  402130:       ba 07 00 00 00          mov    $0x7,%edx
  402135:       be 00 00 10 00          mov    $0x100000,%esi
  40213a:       bf 00 60 58 55          mov    $0x55586000,%edi
  40213f:       e8 ac eb ff ff          callq  400cf0 <mmap@plt>
  402144:       48 89 c3                mov    %rax,%rbx
  402147:       48 3d 00 60 58 55       cmp    $0x55586000,%rax
  40214d:       74 39                   je     402188 <stable_launch+0x71>
  40214f:       be 00 00 10 00          mov    $0x100000,%esi
  402154:       48 89 c7                mov    %rax,%rdi
  402157:       e8 74 ec ff ff          callq  400dd0 <munmap@plt>
  40215c:       b9 00 60 58 55          mov    $0x55586000,%ecx
  402161:       48 8d 15 d8 14 00 00    lea    0x14d8(%rip),%rdx        # 403640 <_IO_stdin_used+0x6d0>
  402168:       be 01 00 00 00          mov    $0x1,%esi
  40216d:       48 8b 3d 4c 33 20 00    mov    0x20334c(%rip),%rdi        # 6054c0 <stderr@@GLIBC_2.2.5>
  402174:       b8 00 00 00 00          mov    $0x0,%eax
  402179:       e8 d2 ec ff ff          callq  400e50 <__fprintf_chk@plt>
  40217e:       bf 01 00 00 00          mov    $0x1,%edi
  402183:       e8 a8 ec ff ff          callq  400e30 <exit@plt>
  402188:       48 8d 90 f8 ff 0f 00    lea    0xffff8(%rax),%rdx
  40218f:       48 89 15 9a 3f 20 00    mov    %rdx,0x203f9a(%rip)        # 606130 <stack_top>
  402196:       48 89 e0                mov    %rsp,%rax
  402199:       48 89 d4                mov    %rdx,%rsp
  40219c:       48 89 c2                mov    %rax,%rdx
  40219f:       48 89 15 3a 33 20 00    mov    %rdx,0x20333a(%rip)        # 6054e0 <global_save_stack>
  4021a6:       48 8b 3d 3b 33 20 00    mov    0x20333b(%rip),%rdi        # 6054e8 <global_offset>
  4021ad:       e8 b2 fe ff ff          callq  402064 <launch>
  4021b2:       48 8b 05 27 33 20 00    mov    0x203327(%rip),%rax        # 6054e0 <global_save_stack>
  4021b9:       48 89 c4                mov    %rax,%rsp
  4021bc:       be 00 00 10 00          mov    $0x100000,%esi
  4021c1:       48 89 df                mov    %rbx,%rdi
  4021c4:       e8 07 ec ff ff          callq  400dd0 <munmap@plt>
  4021c9:       5b                      pop    %rbx
  4021ca:       c3                      retq

00000000004021cb <rio_readinitb>:
  4021cb:       89 37                   mov    %esi,(%rdi)
  4021cd:       c7 47 04 00 00 00 00    movl   $0x0,0x4(%rdi)
  4021d4:       48 8d 47 10             lea    0x10(%rdi),%rax
  4021d8:       48 89 47 08             mov    %rax,0x8(%rdi)
  4021dc:       c3                      retq

00000000004021dd <sigalrm_handler>:
  4021dd:       48 83 ec 08             sub    $0x8,%rsp
  4021e1:       b9 00 00 00 00          mov    $0x0,%ecx
  4021e6:       48 8d 15 93 14 00 00    lea    0x1493(%rip),%rdx        # 403680 <trans_char+0x10>
  4021ed:       be 01 00 00 00          mov    $0x1,%esi
  4021f2:       48 8b 3d c7 32 20 00    mov    0x2032c7(%rip),%rdi        # 6054c0 <stderr@@GLIBC_2.2.5>
  4021f9:       b8 00 00 00 00          mov    $0x0,%eax
  4021fe:       e8 4d ec ff ff          callq  400e50 <__fprintf_chk@plt>
  402203:       bf 01 00 00 00          mov    $0x1,%edi
  402208:       e8 23 ec ff ff          callq  400e30 <exit@plt>

000000000040220d <rio_writen>:
  40220d:       41 55                   push   %r13
  40220f:       41 54                   push   %r12
  402211:       55                      push   %rbp
  402212:       53                      push   %rbx
  402213:       48 83 ec 08             sub    $0x8,%rsp
  402217:       41 89 fc                mov    %edi,%r12d
  40221a:       48 89 f5                mov    %rsi,%rbp
  40221d:       49 89 d5                mov    %rdx,%r13
  402220:       48 89 d3                mov    %rdx,%rbx
  402223:       eb 28                   jmp    40224d <rio_writen+0x40>
  402225:       48 89 da                mov    %rbx,%rdx
  402228:       48 89 ee                mov    %rbp,%rsi
  40222b:       44 89 e7                mov    %r12d,%edi
  40222e:       e8 9d ea ff ff          callq  400cd0 <write@plt>
  402233:       48 85 c0                test   %rax,%rax
  402236:       7f 0f                   jg     402247 <rio_writen+0x3a>
  402238:       e8 43 ea ff ff          callq  400c80 <__errno_location@plt>
  40223d:       83 38 04                cmpl   $0x4,(%rax)
  402240:       75 15                   jne    402257 <rio_writen+0x4a>
  402242:       b8 00 00 00 00          mov    $0x0,%eax
  402247:       48 29 c3                sub    %rax,%rbx
  40224a:       48 01 c5                add    %rax,%rbp
  40224d:       48 85 db                test   %rbx,%rbx
  402250:       75 d3                   jne    402225 <rio_writen+0x18>
  402252:       4c 89 e8                mov    %r13,%rax
  402255:       eb 07                   jmp    40225e <rio_writen+0x51>
  402257:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  40225e:       48 83 c4 08             add    $0x8,%rsp
  402262:       5b                      pop    %rbx
  402263:       5d                      pop    %rbp
  402264:       41 5c                   pop    %r12
  402266:       41 5d                   pop    %r13
  402268:       c3                      retq

0000000000402269 <rio_read>:
  402269:       41 55                   push   %r13
  40226b:       41 54                   push   %r12
  40226d:       55                      push   %rbp
  40226e:       53                      push   %rbx
  40226f:       48 83 ec 08             sub    $0x8,%rsp
  402273:       48 89 fb                mov    %rdi,%rbx
  402276:       49 89 f5                mov    %rsi,%r13
  402279:       49 89 d4                mov    %rdx,%r12
  40227c:       eb 2e                   jmp    4022ac <rio_read+0x43>
  40227e:       48 8d 6b 10             lea    0x10(%rbx),%rbp
  402282:       8b 3b                   mov    (%rbx),%edi
  402284:       ba 00 20 00 00          mov    $0x2000,%edx
  402289:       48 89 ee                mov    %rbp,%rsi
  40228c:       e8 9f ea ff ff          callq  400d30 <read@plt>
  402291:       89 43 04                mov    %eax,0x4(%rbx)
  402294:       85 c0                   test   %eax,%eax
  402296:       79 0c                   jns    4022a4 <rio_read+0x3b>
  402298:       e8 e3 e9 ff ff          callq  400c80 <__errno_location@plt>
  40229d:       83 38 04                cmpl   $0x4,(%rax)
  4022a0:       74 0a                   je     4022ac <rio_read+0x43>
  4022a2:       eb 37                   jmp    4022db <rio_read+0x72>
  4022a4:       85 c0                   test   %eax,%eax
  4022a6:       74 3c                   je     4022e4 <rio_read+0x7b>
  4022a8:       48 89 6b 08             mov    %rbp,0x8(%rbx)
  4022ac:       8b 6b 04                mov    0x4(%rbx),%ebp
  4022af:       85 ed                   test   %ebp,%ebp
  4022b1:       7e cb                   jle    40227e <rio_read+0x15>
  4022b3:       89 e8                   mov    %ebp,%eax
  4022b5:       49 39 c4                cmp    %rax,%r12
  4022b8:       77 03                   ja     4022bd <rio_read+0x54>
  4022ba:       44 89 e5                mov    %r12d,%ebp
  4022bd:       4c 63 e5                movslq %ebp,%r12
  4022c0:       48 8b 73 08             mov    0x8(%rbx),%rsi
  4022c4:       4c 89 e2                mov    %r12,%rdx
  4022c7:       4c 89 ef                mov    %r13,%rdi
  4022ca:       e8 b1 ea ff ff          callq  400d80 <memcpy@plt>
  4022cf:       4c 01 63 08             add    %r12,0x8(%rbx)
  4022d3:       29 6b 04                sub    %ebp,0x4(%rbx)
  4022d6:       4c 89 e0                mov    %r12,%rax
  4022d9:       eb 0e                   jmp    4022e9 <rio_read+0x80>
  4022db:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  4022e2:       eb 05                   jmp    4022e9 <rio_read+0x80>
  4022e4:       b8 00 00 00 00          mov    $0x0,%eax
  4022e9:       48 83 c4 08             add    $0x8,%rsp
  4022ed:       5b                      pop    %rbx
  4022ee:       5d                      pop    %rbp
  4022ef:       41 5c                   pop    %r12
  4022f1:       41 5d                   pop    %r13
  4022f3:       c3                      retq

00000000004022f4 <rio_readlineb>:
  4022f4:       41 55                   push   %r13
  4022f6:       41 54                   push   %r12
  4022f8:       55                      push   %rbp
  4022f9:       53                      push   %rbx
  4022fa:       48 83 ec 18             sub    $0x18,%rsp
  4022fe:       49 89 fd                mov    %rdi,%r13
  402301:       48 89 f5                mov    %rsi,%rbp
  402304:       49 89 d4                mov    %rdx,%r12
  402307:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  40230e:       00 00
  402310:       48 89 44 24 08          mov    %rax,0x8(%rsp)
  402315:       31 c0                   xor    %eax,%eax
  402317:       bb 01 00 00 00          mov    $0x1,%ebx
  40231c:       eb 3f                   jmp    40235d <rio_readlineb+0x69>
  40231e:       48 8d 74 24 07          lea    0x7(%rsp),%rsi
  402323:       ba 01 00 00 00          mov    $0x1,%edx
  402328:       4c 89 ef                mov    %r13,%rdi
  40232b:       e8 39 ff ff ff          callq  402269 <rio_read>
  402330:       83 f8 01                cmp    $0x1,%eax
  402333:       75 15                   jne    40234a <rio_readlineb+0x56>
  402335:       48 8d 45 01             lea    0x1(%rbp),%rax
  402339:       0f b6 54 24 07          movzbl 0x7(%rsp),%edx
  40233e:       88 55 00                mov    %dl,0x0(%rbp)
  402341:       80 7c 24 07 0a          cmpb   $0xa,0x7(%rsp)
  402346:       75 0e                   jne    402356 <rio_readlineb+0x62>
  402348:       eb 1a                   jmp    402364 <rio_readlineb+0x70>
  40234a:       85 c0                   test   %eax,%eax
  40234c:       75 22                   jne    402370 <rio_readlineb+0x7c>
  40234e:       48 83 fb 01             cmp    $0x1,%rbx
  402352:       75 13                   jne    402367 <rio_readlineb+0x73>
  402354:       eb 23                   jmp    402379 <rio_readlineb+0x85>
  402356:       48 83 c3 01             add    $0x1,%rbx
  40235a:       48 89 c5                mov    %rax,%rbp
  40235d:       4c 39 e3                cmp    %r12,%rbx
  402360:       72 bc                   jb     40231e <rio_readlineb+0x2a>
  402362:       eb 03                   jmp    402367 <rio_readlineb+0x73>
  402364:       48 89 c5                mov    %rax,%rbp
  402367:       c6 45 00 00             movb   $0x0,0x0(%rbp)
  40236b:       48 89 d8                mov    %rbx,%rax
  40236e:       eb 0e                   jmp    40237e <rio_readlineb+0x8a>
  402370:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  402377:       eb 05                   jmp    40237e <rio_readlineb+0x8a>
  402379:       b8 00 00 00 00          mov    $0x0,%eax
  40237e:       48 8b 4c 24 08          mov    0x8(%rsp),%rcx
  402383:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
  40238a:       00 00
  40238c:       74 05                   je     402393 <rio_readlineb+0x9f>
  40238e:       e8 4d e9 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402393:       48 83 c4 18             add    $0x18,%rsp
  402397:       5b                      pop    %rbx
  402398:       5d                      pop    %rbp
  402399:       41 5c                   pop    %r12
  40239b:       41 5d                   pop    %r13
  40239d:       c3                      retq

000000000040239e <urlencode>:
  40239e:       41 54                   push   %r12
  4023a0:       55                      push   %rbp
  4023a1:       53                      push   %rbx
  4023a2:       48 83 ec 10             sub    $0x10,%rsp
  4023a6:       48 89 fb                mov    %rdi,%rbx
  4023a9:       48 89 f5                mov    %rsi,%rbp
  4023ac:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4023b3:       00 00
  4023b5:       48 89 44 24 08          mov    %rax,0x8(%rsp)
  4023ba:       31 c0                   xor    %eax,%eax
  4023bc:       48 c7 c1 ff ff ff ff    mov    $0xffffffffffffffff,%rcx
  4023c3:       f2 ae                   repnz scas %es:(%rdi),%al
  4023c5:       48 f7 d1                not    %rcx
  4023c8:       8d 41 ff                lea    -0x1(%rcx),%eax
  4023cb:       e9 ac 00 00 00          jmpq   40247c <urlencode+0xde>
  4023d0:       44 0f b6 03             movzbl (%rbx),%r8d
  4023d4:       41 80 f8 2a             cmp    $0x2a,%r8b
  4023d8:       0f 94 c2                sete   %dl
  4023db:       41 80 f8 2d             cmp    $0x2d,%r8b
  4023df:       0f 94 c0                sete   %al
  4023e2:       08 c2                   or     %al,%dl
  4023e4:       75 24                   jne    40240a <urlencode+0x6c>
  4023e6:       41 80 f8 2e             cmp    $0x2e,%r8b
  4023ea:       74 1e                   je     40240a <urlencode+0x6c>
  4023ec:       41 80 f8 5f             cmp    $0x5f,%r8b
  4023f0:       74 18                   je     40240a <urlencode+0x6c>
  4023f2:       41 8d 40 d0             lea    -0x30(%r8),%eax
  4023f6:       3c 09                   cmp    $0x9,%al
  4023f8:       76 10                   jbe    40240a <urlencode+0x6c>
  4023fa:       41 8d 40 bf             lea    -0x41(%r8),%eax
  4023fe:       3c 19                   cmp    $0x19,%al
  402400:       76 08                   jbe    40240a <urlencode+0x6c>
  402402:       41 8d 40 9f             lea    -0x61(%r8),%eax
  402406:       3c 19                   cmp    $0x19,%al
  402408:       77 0a                   ja     402414 <urlencode+0x76>
  40240a:       44 88 45 00             mov    %r8b,0x0(%rbp)
  40240e:       48 8d 6d 01             lea    0x1(%rbp),%rbp
  402412:       eb 61                   jmp    402475 <urlencode+0xd7>
  402414:       41 80 f8 20             cmp    $0x20,%r8b
  402418:       75 0a                   jne    402424 <urlencode+0x86>
  40241a:       c6 45 00 2b             movb   $0x2b,0x0(%rbp)
  40241e:       48 8d 6d 01             lea    0x1(%rbp),%rbp
  402422:       eb 51                   jmp    402475 <urlencode+0xd7>
  402424:       41 8d 40 e0             lea    -0x20(%r8),%eax
  402428:       3c 5f                   cmp    $0x5f,%al
  40242a:       0f 96 c2                setbe  %dl
  40242d:       41 80 f8 09             cmp    $0x9,%r8b
  402431:       0f 94 c0                sete   %al
  402434:       08 c2                   or     %al,%dl
  402436:       74 52                   je     40248a <urlencode+0xec>
  402438:       48 89 e7                mov    %rsp,%rdi
  40243b:       45 0f b6 c0             movzbl %r8b,%r8d
  40243f:       48 8d 0d d2 12 00 00    lea    0x12d2(%rip),%rcx        # 403718 <trans_char+0xa8>
  402446:       ba 08 00 00 00          mov    $0x8,%edx
  40244b:       be 01 00 00 00          mov    $0x1,%esi
  402450:       b8 00 00 00 00          mov    $0x0,%eax
  402455:       e8 06 ea ff ff          callq  400e60 <__sprintf_chk@plt>
  40245a:       0f b6 04 24             movzbl (%rsp),%eax
  40245e:       88 45 00                mov    %al,0x0(%rbp)
  402461:       0f b6 44 24 01          movzbl 0x1(%rsp),%eax
  402466:       88 45 01                mov    %al,0x1(%rbp)
  402469:       0f b6 44 24 02          movzbl 0x2(%rsp),%eax
  40246e:       88 45 02                mov    %al,0x2(%rbp)
  402471:       48 8d 6d 03             lea    0x3(%rbp),%rbp
  402475:       48 83 c3 01             add    $0x1,%rbx
  402479:       44 89 e0                mov    %r12d,%eax
  40247c:       44 8d 60 ff             lea    -0x1(%rax),%r12d
  402480:       85 c0                   test   %eax,%eax
  402482:       0f 85 48 ff ff ff       jne    4023d0 <urlencode+0x32>
  402488:       eb 05                   jmp    40248f <urlencode+0xf1>
  40248a:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  40248f:       48 8b 74 24 08          mov    0x8(%rsp),%rsi
  402494:       64 48 33 34 25 28 00    xor    %fs:0x28,%rsi
  40249b:       00 00
  40249d:       74 05                   je     4024a4 <urlencode+0x106>
  40249f:       e8 3c e8 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  4024a4:       48 83 c4 10             add    $0x10,%rsp
  4024a8:       5b                      pop    %rbx
  4024a9:       5d                      pop    %rbp
  4024aa:       41 5c                   pop    %r12
  4024ac:       c3                      retq

00000000004024ad <submitr>:
  4024ad:       41 57                   push   %r15
  4024af:       41 56                   push   %r14
  4024b1:       41 55                   push   %r13
  4024b3:       41 54                   push   %r12
  4024b5:       55                      push   %rbp
  4024b6:       53                      push   %rbx
  4024b7:       48 81 ec 68 a0 00 00    sub    $0xa068,%rsp
  4024be:       49 89 fd                mov    %rdi,%r13
  4024c1:       89 74 24 14             mov    %esi,0x14(%rsp)
  4024c5:       49 89 d7                mov    %rdx,%r15
  4024c8:       48 89 4c 24 08          mov    %rcx,0x8(%rsp)
  4024cd:       4c 89 44 24 18          mov    %r8,0x18(%rsp)
  4024d2:       4d 89 ce                mov    %r9,%r14
  4024d5:       48 8b 9c 24 a0 a0 00    mov    0xa0a0(%rsp),%rbx
  4024dc:       00
  4024dd:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4024e4:       00 00
  4024e6:       48 89 84 24 58 a0 00    mov    %rax,0xa058(%rsp)
  4024ed:       00
  4024ee:       31 c0                   xor    %eax,%eax
  4024f0:       c7 44 24 2c 00 00 00    movl   $0x0,0x2c(%rsp)
  4024f7:       00
  4024f8:       ba 00 00 00 00          mov    $0x0,%edx
  4024fd:       be 01 00 00 00          mov    $0x1,%esi
  402502:       bf 02 00 00 00          mov    $0x2,%edi
  402507:       e8 64 e9 ff ff          callq  400e70 <socket@plt>
  40250c:       85 c0                   test   %eax,%eax
  40250e:       79 4e                   jns    40255e <submitr+0xb1>
  402510:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402517:       3a 20 43
  40251a:       48 89 03                mov    %rax,(%rbx)
  40251d:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402524:       20 75 6e
  402527:       48 89 43 08             mov    %rax,0x8(%rbx)
  40252b:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402532:       74 6f 20
  402535:       48 89 43 10             mov    %rax,0x10(%rbx)
  402539:       48 b8 63 72 65 61 74    movabs $0x7320657461657263,%rax
  402540:       65 20 73
  402543:       48 89 43 18             mov    %rax,0x18(%rbx)
  402547:       c7 43 20 6f 63 6b 65    movl   $0x656b636f,0x20(%rbx)
  40254e:       66 c7 43 24 74 00       movw   $0x74,0x24(%rbx)
  402554:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402559:       e9 77 06 00 00          jmpq   402bd5 <submitr+0x728>
  40255e:       89 c5                   mov    %eax,%ebp
  402560:       4c 89 ef                mov    %r13,%rdi
  402563:       e8 e8 e7 ff ff          callq  400d50 <gethostbyname@plt>
  402568:       48 85 c0                test   %rax,%rax
  40256b:       75 67                   jne    4025d4 <submitr+0x127>
  40256d:       48 b8 45 72 72 6f 72    movabs $0x44203a726f727245,%rax
  402574:       3a 20 44
  402577:       48 89 03                mov    %rax,(%rbx)
  40257a:       48 b8 4e 53 20 69 73    movabs $0x6e7520736920534e,%rax
  402581:       20 75 6e
  402584:       48 89 43 08             mov    %rax,0x8(%rbx)
  402588:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  40258f:       74 6f 20
  402592:       48 89 43 10             mov    %rax,0x10(%rbx)
  402596:       48 b8 72 65 73 6f 6c    movabs $0x2065766c6f736572,%rax
  40259d:       76 65 20
  4025a0:       48 89 43 18             mov    %rax,0x18(%rbx)
  4025a4:       48 b8 73 65 72 76 65    movabs $0x6120726576726573,%rax
  4025ab:       72 20 61
  4025ae:       48 89 43 20             mov    %rax,0x20(%rbx)
  4025b2:       c7 43 28 64 64 72 65    movl   $0x65726464,0x28(%rbx)
  4025b9:       66 c7 43 2c 73 73       movw   $0x7373,0x2c(%rbx)
  4025bf:       c6 43 2e 00             movb   $0x0,0x2e(%rbx)
  4025c3:       89 ef                   mov    %ebp,%edi
  4025c5:       e8 56 e7 ff ff          callq  400d20 <close@plt>
  4025ca:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  4025cf:       e9 01 06 00 00          jmpq   402bd5 <submitr+0x728>
  4025d4:       4c 8d 64 24 30          lea    0x30(%rsp),%r12
  4025d9:       48 c7 44 24 30 00 00    movq   $0x0,0x30(%rsp)
  4025e0:       00 00
  4025e2:       48 c7 44 24 38 00 00    movq   $0x0,0x38(%rsp)
  4025e9:       00 00
  4025eb:       66 c7 44 24 30 02 00    movw   $0x2,0x30(%rsp)
  4025f2:       48 63 50 14             movslq 0x14(%rax),%rdx
  4025f6:       48 8b 40 18             mov    0x18(%rax),%rax
  4025fa:       48 8b 30                mov    (%rax),%rsi
  4025fd:       48 8d 7c 24 34          lea    0x34(%rsp),%rdi
  402602:       b9 0c 00 00 00          mov    $0xc,%ecx
  402607:       e8 54 e7 ff ff          callq  400d60 <__memmove_chk@plt>
  40260c:       0f b7 44 24 14          movzwl 0x14(%rsp),%eax
  402611:       66 c1 c8 08             ror    $0x8,%ax
  402615:       66 89 44 24 32          mov    %ax,0x32(%rsp)
  40261a:       ba 10 00 00 00          mov    $0x10,%edx
  40261f:       4c 89 e6                mov    %r12,%rsi
  402622:       89 ef                   mov    %ebp,%edi
  402624:       e8 17 e8 ff ff          callq  400e40 <connect@plt>
  402629:       85 c0                   test   %eax,%eax
  40262b:       79 59                   jns    402686 <submitr+0x1d9>
  40262d:       48 b8 45 72 72 6f 72    movabs $0x55203a726f727245,%rax
  402634:       3a 20 55
  402637:       48 89 03                mov    %rax,(%rbx)
  40263a:       48 b8 6e 61 62 6c 65    movabs $0x6f7420656c62616e,%rax
  402641:       20 74 6f
  402644:       48 89 43 08             mov    %rax,0x8(%rbx)
  402648:       48 b8 20 63 6f 6e 6e    movabs $0x7463656e6e6f6320,%rax
  40264f:       65 63 74
  402652:       48 89 43 10             mov    %rax,0x10(%rbx)
  402656:       48 b8 20 74 6f 20 74    movabs $0x20656874206f7420,%rax
  40265d:       68 65 20
  402660:       48 89 43 18             mov    %rax,0x18(%rbx)
  402664:       c7 43 20 73 65 72 76    movl   $0x76726573,0x20(%rbx)
  40266b:       66 c7 43 24 65 72       movw   $0x7265,0x24(%rbx)
  402671:       c6 43 26 00             movb   $0x0,0x26(%rbx)
  402675:       89 ef                   mov    %ebp,%edi
  402677:       e8 a4 e6 ff ff          callq  400d20 <close@plt>
  40267c:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402681:       e9 4f 05 00 00          jmpq   402bd5 <submitr+0x728>
  402686:       48 c7 c6 ff ff ff ff    mov    $0xffffffffffffffff,%rsi
  40268d:       b8 00 00 00 00          mov    $0x0,%eax
  402692:       48 89 f1                mov    %rsi,%rcx
  402695:       4c 89 f7                mov    %r14,%rdi
  402698:       f2 ae                   repnz scas %es:(%rdi),%al
  40269a:       48 89 ca                mov    %rcx,%rdx
  40269d:       48 f7 d2                not    %rdx
  4026a0:       48 89 f1                mov    %rsi,%rcx
  4026a3:       4c 89 ff                mov    %r15,%rdi
  4026a6:       f2 ae                   repnz scas %es:(%rdi),%al
  4026a8:       48 f7 d1                not    %rcx
  4026ab:       49 89 c8                mov    %rcx,%r8
  4026ae:       48 89 f1                mov    %rsi,%rcx
  4026b1:       48 8b 7c 24 08          mov    0x8(%rsp),%rdi
  4026b6:       f2 ae                   repnz scas %es:(%rdi),%al
  4026b8:       48 f7 d1                not    %rcx
  4026bb:       4d 8d 44 08 fe          lea    -0x2(%r8,%rcx,1),%r8
  4026c0:       48 89 f1                mov    %rsi,%rcx
  4026c3:       48 8b 7c 24 18          mov    0x18(%rsp),%rdi
  4026c8:       f2 ae                   repnz scas %es:(%rdi),%al
  4026ca:       48 89 c8                mov    %rcx,%rax
  4026cd:       48 f7 d0                not    %rax
  4026d0:       49 8d 4c 00 ff          lea    -0x1(%r8,%rax,1),%rcx
  4026d5:       48 8d 44 52 fd          lea    -0x3(%rdx,%rdx,2),%rax
  4026da:       48 8d 84 01 80 00 00    lea    0x80(%rcx,%rax,1),%rax
  4026e1:       00
  4026e2:       48 3d 00 20 00 00       cmp    $0x2000,%rax
  4026e8:       76 72                   jbe    40275c <submitr+0x2af>
  4026ea:       48 b8 45 72 72 6f 72    movabs $0x52203a726f727245,%rax
  4026f1:       3a 20 52
  4026f4:       48 89 03                mov    %rax,(%rbx)
  4026f7:       48 b8 65 73 75 6c 74    movabs $0x747320746c757365,%rax
  4026fe:       20 73 74
  402701:       48 89 43 08             mov    %rax,0x8(%rbx)
  402705:       48 b8 72 69 6e 67 20    movabs $0x6f6f7420676e6972,%rax
  40270c:       74 6f 6f
  40270f:       48 89 43 10             mov    %rax,0x10(%rbx)
  402713:       48 b8 20 6c 61 72 67    movabs $0x202e656772616c20,%rax
  40271a:       65 2e 20
  40271d:       48 89 43 18             mov    %rax,0x18(%rbx)
  402721:       48 b8 49 6e 63 72 65    movabs $0x6573616572636e49,%rax
  402728:       61 73 65
  40272b:       48 89 43 20             mov    %rax,0x20(%rbx)
  40272f:       48 b8 20 53 55 42 4d    movabs $0x5254494d42555320,%rax
  402736:       49 54 52
  402739:       48 89 43 28             mov    %rax,0x28(%rbx)
  40273d:       48 b8 5f 4d 41 58 42    movabs $0x46554258414d5f,%rax
  402744:       55 46 00
  402747:       48 89 43 30             mov    %rax,0x30(%rbx)
  40274b:       89 ef                   mov    %ebp,%edi
  40274d:       e8 ce e5 ff ff          callq  400d20 <close@plt>
  402752:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402757:       e9 79 04 00 00          jmpq   402bd5 <submitr+0x728>
  40275c:       48 8d b4 24 50 40 00    lea    0x4050(%rsp),%rsi
  402763:       00
  402764:       b9 00 04 00 00          mov    $0x400,%ecx
  402769:       b8 00 00 00 00          mov    $0x0,%eax
  40276e:       48 89 f7                mov    %rsi,%rdi
  402771:       f3 48 ab                rep stos %rax,%es:(%rdi)
  402774:       4c 89 f7                mov    %r14,%rdi
  402777:       e8 22 fc ff ff          callq  40239e <urlencode>
  40277c:       85 c0                   test   %eax,%eax
  40277e:       0f 89 8a 00 00 00       jns    40280e <submitr+0x361>
  402784:       48 b8 45 72 72 6f 72    movabs $0x52203a726f727245,%rax
  40278b:       3a 20 52
  40278e:       48 89 03                mov    %rax,(%rbx)
  402791:       48 b8 65 73 75 6c 74    movabs $0x747320746c757365,%rax
  402798:       20 73 74
  40279b:       48 89 43 08             mov    %rax,0x8(%rbx)
  40279f:       48 b8 72 69 6e 67 20    movabs $0x6e6f6320676e6972,%rax
  4027a6:       63 6f 6e
  4027a9:       48 89 43 10             mov    %rax,0x10(%rbx)
  4027ad:       48 b8 74 61 69 6e 73    movabs $0x6e6120736e696174,%rax
  4027b4:       20 61 6e
  4027b7:       48 89 43 18             mov    %rax,0x18(%rbx)
  4027bb:       48 b8 20 69 6c 6c 65    movabs $0x6c6167656c6c6920,%rax
  4027c2:       67 61 6c
  4027c5:       48 89 43 20             mov    %rax,0x20(%rbx)
  4027c9:       48 b8 20 6f 72 20 75    movabs $0x72706e7520726f20,%rax
  4027d0:       6e 70 72
  4027d3:       48 89 43 28             mov    %rax,0x28(%rbx)
  4027d7:       48 b8 69 6e 74 61 62    movabs $0x20656c6261746e69,%rax
  4027de:       6c 65 20
  4027e1:       48 89 43 30             mov    %rax,0x30(%rbx)
  4027e5:       48 b8 63 68 61 72 61    movabs $0x6574636172616863,%rax
  4027ec:       63 74 65
  4027ef:       48 89 43 38             mov    %rax,0x38(%rbx)
  4027f3:       66 c7 43 40 72 2e       movw   $0x2e72,0x40(%rbx)
  4027f9:       c6 43 42 00             movb   $0x0,0x42(%rbx)
  4027fd:       89 ef                   mov    %ebp,%edi
  4027ff:       e8 1c e5 ff ff          callq  400d20 <close@plt>
  402804:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402809:       e9 c7 03 00 00          jmpq   402bd5 <submitr+0x728>
  40280e:       4c 8d a4 24 50 20 00    lea    0x2050(%rsp),%r12
  402815:       00
  402816:       41 55                   push   %r13
  402818:       48 8d 84 24 58 40 00    lea    0x4058(%rsp),%rax
  40281f:       00
  402820:       50                      push   %rax
  402821:       4d 89 f9                mov    %r15,%r9
  402824:       4c 8b 44 24 18          mov    0x18(%rsp),%r8
  402829:       48 8d 0d 78 0e 00 00    lea    0xe78(%rip),%rcx        # 4036a8 <trans_char+0x38>
  402830:       ba 00 20 00 00          mov    $0x2000,%edx
  402835:       be 01 00 00 00          mov    $0x1,%esi
  40283a:       4c 89 e7                mov    %r12,%rdi
  40283d:       b8 00 00 00 00          mov    $0x0,%eax
  402842:       e8 19 e6 ff ff          callq  400e60 <__sprintf_chk@plt>
  402847:       b8 00 00 00 00          mov    $0x0,%eax
  40284c:       48 c7 c1 ff ff ff ff    mov    $0xffffffffffffffff,%rcx
  402853:       4c 89 e7                mov    %r12,%rdi
  402856:       f2 ae                   repnz scas %es:(%rdi),%al
  402858:       48 f7 d1                not    %rcx
  40285b:       48 8d 51 ff             lea    -0x1(%rcx),%rdx
  40285f:       4c 89 e6                mov    %r12,%rsi
  402862:       89 ef                   mov    %ebp,%edi
  402864:       e8 a4 f9 ff ff          callq  40220d <rio_writen>
  402869:       48 83 c4 10             add    $0x10,%rsp
  40286d:       48 85 c0                test   %rax,%rax
  402870:       79 6e                   jns    4028e0 <submitr+0x433>
  402872:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402879:       3a 20 43
  40287c:       48 89 03                mov    %rax,(%rbx)
  40287f:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402886:       20 75 6e
  402889:       48 89 43 08             mov    %rax,0x8(%rbx)
  40288d:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402894:       74 6f 20
  402897:       48 89 43 10             mov    %rax,0x10(%rbx)
  40289b:       48 b8 77 72 69 74 65    movabs $0x6f74206574697277,%rax
  4028a2:       20 74 6f
  4028a5:       48 89 43 18             mov    %rax,0x18(%rbx)
  4028a9:       48 b8 20 74 68 65 20    movabs $0x7365722065687420,%rax
  4028b0:       72 65 73
  4028b3:       48 89 43 20             mov    %rax,0x20(%rbx)
  4028b7:       48 b8 75 6c 74 20 73    movabs $0x7672657320746c75,%rax
  4028be:       65 72 76
  4028c1:       48 89 43 28             mov    %rax,0x28(%rbx)
  4028c5:       66 c7 43 30 65 72       movw   $0x7265,0x30(%rbx)
  4028cb:       c6 43 32 00             movb   $0x0,0x32(%rbx)
  4028cf:       89 ef                   mov    %ebp,%edi
  4028d1:       e8 4a e4 ff ff          callq  400d20 <close@plt>
  4028d6:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  4028db:       e9 f5 02 00 00          jmpq   402bd5 <submitr+0x728>
  4028e0:       4c 8d 64 24 40          lea    0x40(%rsp),%r12
  4028e5:       89 ee                   mov    %ebp,%esi
  4028e7:       4c 89 e7                mov    %r12,%rdi
  4028ea:       e8 dc f8 ff ff          callq  4021cb <rio_readinitb>
  4028ef:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  4028f6:       00
  4028f7:       ba 00 20 00 00          mov    $0x2000,%edx
  4028fc:       4c 89 e7                mov    %r12,%rdi
  4028ff:       e8 f0 f9 ff ff          callq  4022f4 <rio_readlineb>
  402904:       48 85 c0                test   %rax,%rax
  402907:       7f 7d                   jg     402986 <submitr+0x4d9>
  402909:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402910:       3a 20 43
  402913:       48 89 03                mov    %rax,(%rbx)
  402916:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  40291d:       20 75 6e
  402920:       48 89 43 08             mov    %rax,0x8(%rbx)
  402924:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  40292b:       74 6f 20
  40292e:       48 89 43 10             mov    %rax,0x10(%rbx)
  402932:       48 b8 72 65 61 64 20    movabs $0x7269662064616572,%rax
  402939:       66 69 72
  40293c:       48 89 43 18             mov    %rax,0x18(%rbx)
  402940:       48 b8 73 74 20 68 65    movabs $0x6564616568207473,%rax
  402947:       61 64 65
  40294a:       48 89 43 20             mov    %rax,0x20(%rbx)
  40294e:       48 b8 72 20 66 72 6f    movabs $0x72206d6f72662072,%rax
  402955:       6d 20 72
  402958:       48 89 43 28             mov    %rax,0x28(%rbx)
  40295c:       48 b8 65 73 75 6c 74    movabs $0x657320746c757365,%rax
  402963:       20 73 65
  402966:       48 89 43 30             mov    %rax,0x30(%rbx)
  40296a:       c7 43 38 72 76 65 72    movl   $0x72657672,0x38(%rbx)
  402971:       c6 43 3c 00             movb   $0x0,0x3c(%rbx)
  402975:       89 ef                   mov    %ebp,%edi
  402977:       e8 a4 e3 ff ff          callq  400d20 <close@plt>
  40297c:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402981:       e9 4f 02 00 00          jmpq   402bd5 <submitr+0x728>
  402986:       48 8d 4c 24 2c          lea    0x2c(%rsp),%rcx
  40298b:       48 8d 94 24 50 60 00    lea    0x6050(%rsp),%rdx
  402992:       00
  402993:       48 8d bc 24 50 20 00    lea    0x2050(%rsp),%rdi
  40299a:       00
  40299b:       4c 8d 84 24 50 80 00    lea    0x8050(%rsp),%r8
  4029a2:       00
  4029a3:       48 8d 35 75 0d 00 00    lea    0xd75(%rip),%rsi        # 40371f <trans_char+0xaf>
  4029aa:       b8 00 00 00 00          mov    $0x0,%eax
  4029af:       e8 0c e4 ff ff          callq  400dc0 <__isoc99_sscanf@plt>
  4029b4:       e9 95 00 00 00          jmpq   402a4e <submitr+0x5a1>
  4029b9:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  4029c0:       00
  4029c1:       48 8d 7c 24 40          lea    0x40(%rsp),%rdi
  4029c6:       ba 00 20 00 00          mov    $0x2000,%edx
  4029cb:       e8 24 f9 ff ff          callq  4022f4 <rio_readlineb>
  4029d0:       48 85 c0                test   %rax,%rax
  4029d3:       7f 79                   jg     402a4e <submitr+0x5a1>
  4029d5:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  4029dc:       3a 20 43
  4029df:       48 89 03                mov    %rax,(%rbx)
  4029e2:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  4029e9:       20 75 6e
  4029ec:       48 89 43 08             mov    %rax,0x8(%rbx)
  4029f0:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  4029f7:       74 6f 20
  4029fa:       48 89 43 10             mov    %rax,0x10(%rbx)
  4029fe:       48 b8 72 65 61 64 20    movabs $0x6165682064616572,%rax
  402a05:       68 65 61
  402a08:       48 89 43 18             mov    %rax,0x18(%rbx)
  402a0c:       48 b8 64 65 72 73 20    movabs $0x6f72662073726564,%rax
  402a13:       66 72 6f
  402a16:       48 89 43 20             mov    %rax,0x20(%rbx)
  402a1a:       48 b8 6d 20 74 68 65    movabs $0x657220656874206d,%rax
  402a21:       20 72 65
  402a24:       48 89 43 28             mov    %rax,0x28(%rbx)
  402a28:       48 b8 73 75 6c 74 20    movabs $0x72657320746c7573,%rax
  402a2f:       73 65 72
  402a32:       48 89 43 30             mov    %rax,0x30(%rbx)
  402a36:       c7 43 38 76 65 72 00    movl   $0x726576,0x38(%rbx)
  402a3d:       89 ef                   mov    %ebp,%edi
  402a3f:       e8 dc e2 ff ff          callq  400d20 <close@plt>
  402a44:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402a49:       e9 87 01 00 00          jmpq   402bd5 <submitr+0x728>
  402a4e:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402a55:       00
  402a56:       b9 03 00 00 00          mov    $0x3,%ecx
  402a5b:       48 8d 3d d4 0c 00 00    lea    0xcd4(%rip),%rdi        # 403736 <trans_char+0xc6>
  402a62:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402a64:       0f 97 c2                seta   %dl
  402a67:       0f 92 c0                setb   %al
  402a6a:       38 c2                   cmp    %al,%dl
  402a6c:       0f 85 47 ff ff ff       jne    4029b9 <submitr+0x50c>
  402a72:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402a79:       00
  402a7a:       48 8d 7c 24 40          lea    0x40(%rsp),%rdi
  402a7f:       ba 00 20 00 00          mov    $0x2000,%edx
  402a84:       e8 6b f8 ff ff          callq  4022f4 <rio_readlineb>
  402a89:       48 85 c0                test   %rax,%rax
  402a8c:       0f 8f 83 00 00 00       jg     402b15 <submitr+0x668>
  402a92:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402a99:       3a 20 43
  402a9c:       48 89 03                mov    %rax,(%rbx)
  402a9f:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402aa6:       20 75 6e
  402aa9:       48 89 43 08             mov    %rax,0x8(%rbx)
  402aad:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402ab4:       74 6f 20
  402ab7:       48 89 43 10             mov    %rax,0x10(%rbx)
  402abb:       48 b8 72 65 61 64 20    movabs $0x6174732064616572,%rax
  402ac2:       73 74 61
  402ac5:       48 89 43 18             mov    %rax,0x18(%rbx)
  402ac9:       48 b8 74 75 73 20 6d    movabs $0x7373656d20737574,%rax
  402ad0:       65 73 73
  402ad3:       48 89 43 20             mov    %rax,0x20(%rbx)
  402ad7:       48 b8 61 67 65 20 66    movabs $0x6d6f726620656761,%rax
  402ade:       72 6f 6d
  402ae1:       48 89 43 28             mov    %rax,0x28(%rbx)
  402ae5:       48 b8 20 72 65 73 75    movabs $0x20746c7573657220,%rax
  402aec:       6c 74 20
  402aef:       48 89 43 30             mov    %rax,0x30(%rbx)
  402af3:       c7 43 38 73 65 72 76    movl   $0x76726573,0x38(%rbx)
  402afa:       66 c7 43 3c 65 72       movw   $0x7265,0x3c(%rbx)
  402b00:       c6 43 3e 00             movb   $0x0,0x3e(%rbx)
  402b04:       89 ef                   mov    %ebp,%edi
  402b06:       e8 15 e2 ff ff          callq  400d20 <close@plt>
  402b0b:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402b10:       e9 c0 00 00 00          jmpq   402bd5 <submitr+0x728>
  402b15:       44 8b 44 24 2c          mov    0x2c(%rsp),%r8d
  402b1a:       41 81 f8 c8 00 00 00    cmp    $0xc8,%r8d
  402b21:       74 36                   je     402b59 <submitr+0x6ac>
  402b23:       4c 8d 8c 24 50 80 00    lea    0x8050(%rsp),%r9
  402b2a:       00
  402b2b:       48 8d 0d b6 0b 00 00    lea    0xbb6(%rip),%rcx        # 4036e8 <trans_char+0x78>
  402b32:       48 c7 c2 ff ff ff ff    mov    $0xffffffffffffffff,%rdx
  402b39:       be 01 00 00 00          mov    $0x1,%esi
  402b3e:       48 89 df                mov    %rbx,%rdi
  402b41:       b8 00 00 00 00          mov    $0x0,%eax
  402b46:       e8 15 e3 ff ff          callq  400e60 <__sprintf_chk@plt>
  402b4b:       89 ef                   mov    %ebp,%edi
  402b4d:       e8 ce e1 ff ff          callq  400d20 <close@plt>
  402b52:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402b57:       eb 7c                   jmp    402bd5 <submitr+0x728>
  402b59:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402b60:       00
  402b61:       48 89 df                mov    %rbx,%rdi
  402b64:       e8 47 e1 ff ff          callq  400cb0 <strcpy@plt>
  402b69:       89 ef                   mov    %ebp,%edi
  402b6b:       e8 b0 e1 ff ff          callq  400d20 <close@plt>
  402b70:       b9 04 00 00 00          mov    $0x4,%ecx
  402b75:       48 8d 3d b4 0b 00 00    lea    0xbb4(%rip),%rdi        # 403730 <trans_char+0xc0>
  402b7c:       48 89 de                mov    %rbx,%rsi
  402b7f:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402b81:       0f 97 c0                seta   %al
  402b84:       0f 92 c2                setb   %dl
  402b87:       29 d0                   sub    %edx,%eax
  402b89:       0f be c0                movsbl %al,%eax
  402b8c:       85 c0                   test   %eax,%eax
  402b8e:       74 45                   je     402bd5 <submitr+0x728>
  402b90:       b9 05 00 00 00          mov    $0x5,%ecx
  402b95:       48 8d 3d 98 0b 00 00    lea    0xb98(%rip),%rdi        # 403734 <trans_char+0xc4>
  402b9c:       48 89 de                mov    %rbx,%rsi
  402b9f:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402ba1:       0f 97 c0                seta   %al
  402ba4:       0f 92 c2                setb   %dl
  402ba7:       29 d0                   sub    %edx,%eax
  402ba9:       0f be c0                movsbl %al,%eax
  402bac:       85 c0                   test   %eax,%eax
  402bae:       74 25                   je     402bd5 <submitr+0x728>
  402bb0:       b9 03 00 00 00          mov    $0x3,%ecx
  402bb5:       48 8d 3d 7d 0b 00 00    lea    0xb7d(%rip),%rdi        # 403739 <trans_char+0xc9>
  402bbc:       48 89 de                mov    %rbx,%rsi
  402bbf:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402bc1:       0f 97 c0                seta   %al
  402bc4:       0f 92 c2                setb   %dl
  402bc7:       29 d0                   sub    %edx,%eax
  402bc9:       0f be c0                movsbl %al,%eax
  402bcc:       85 c0                   test   %eax,%eax
  402bce:       74 05                   je     402bd5 <submitr+0x728>
  402bd0:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402bd5:       48 8b 9c 24 58 a0 00    mov    0xa058(%rsp),%rbx
  402bdc:       00
  402bdd:       64 48 33 1c 25 28 00    xor    %fs:0x28,%rbx
  402be4:       00 00
  402be6:       74 05                   je     402bed <submitr+0x740>
  402be8:       e8 f3 e0 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402bed:       48 81 c4 68 a0 00 00    add    $0xa068,%rsp
  402bf4:       5b                      pop    %rbx
  402bf5:       5d                      pop    %rbp
  402bf6:       41 5c                   pop    %r12
  402bf8:       41 5d                   pop    %r13
  402bfa:       41 5e                   pop    %r14
  402bfc:       41 5f                   pop    %r15
  402bfe:       c3                      retq

0000000000402bff <init_timeout>:
  402bff:       85 ff                   test   %edi,%edi
  402c01:       74 25                   je     402c28 <init_timeout+0x29>
  402c03:       53                      push   %rbx
  402c04:       89 fb                   mov    %edi,%ebx
  402c06:       85 ff                   test   %edi,%edi
  402c08:       79 05                   jns    402c0f <init_timeout+0x10>
  402c0a:       bb 00 00 00 00          mov    $0x0,%ebx
  402c0f:       48 8d 35 c7 f5 ff ff    lea    -0xa39(%rip),%rsi        # 4021dd <sigalrm_handler>
  402c16:       bf 0e 00 00 00          mov    $0xe,%edi
  402c1b:       e8 20 e1 ff ff          callq  400d40 <signal@plt>
  402c20:       89 df                   mov    %ebx,%edi
  402c22:       e8 e9 e0 ff ff          callq  400d10 <alarm@plt>
  402c27:       5b                      pop    %rbx
  402c28:       f3 c3                   repz retq

0000000000402c2a <init_driver>:
  402c2a:       41 54                   push   %r12
  402c2c:       55                      push   %rbp
  402c2d:       53                      push   %rbx
  402c2e:       48 83 ec 20             sub    $0x20,%rsp
  402c32:       48 89 fd                mov    %rdi,%rbp
  402c35:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  402c3c:       00 00
  402c3e:       48 89 44 24 18          mov    %rax,0x18(%rsp)
  402c43:       31 c0                   xor    %eax,%eax
  402c45:       be 01 00 00 00          mov    $0x1,%esi
  402c4a:       bf 0d 00 00 00          mov    $0xd,%edi
  402c4f:       e8 ec e0 ff ff          callq  400d40 <signal@plt>
  402c54:       be 01 00 00 00          mov    $0x1,%esi
  402c59:       bf 1d 00 00 00          mov    $0x1d,%edi
  402c5e:       e8 dd e0 ff ff          callq  400d40 <signal@plt>
  402c63:       be 01 00 00 00          mov    $0x1,%esi
  402c68:       bf 1d 00 00 00          mov    $0x1d,%edi
  402c6d:       e8 ce e0 ff ff          callq  400d40 <signal@plt>
  402c72:       ba 00 00 00 00          mov    $0x0,%edx
  402c77:       be 01 00 00 00          mov    $0x1,%esi
  402c7c:       bf 02 00 00 00          mov    $0x2,%edi
  402c81:       e8 ea e1 ff ff          callq  400e70 <socket@plt>
  402c86:       85 c0                   test   %eax,%eax
  402c88:       79 4f                   jns    402cd9 <init_driver+0xaf>
  402c8a:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402c91:       3a 20 43
  402c94:       48 89 45 00             mov    %rax,0x0(%rbp)
  402c98:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402c9f:       20 75 6e
  402ca2:       48 89 45 08             mov    %rax,0x8(%rbp)
  402ca6:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402cad:       74 6f 20
  402cb0:       48 89 45 10             mov    %rax,0x10(%rbp)
  402cb4:       48 b8 63 72 65 61 74    movabs $0x7320657461657263,%rax
  402cbb:       65 20 73
  402cbe:       48 89 45 18             mov    %rax,0x18(%rbp)
  402cc2:       c7 45 20 6f 63 6b 65    movl   $0x656b636f,0x20(%rbp)
  402cc9:       66 c7 45 24 74 00       movw   $0x74,0x24(%rbp)
  402ccf:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402cd4:       e9 2c 01 00 00          jmpq   402e05 <init_driver+0x1db>
  402cd9:       89 c3                   mov    %eax,%ebx
  402cdb:       48 8d 3d 5a 0a 00 00    lea    0xa5a(%rip),%rdi        # 40373c <trans_char+0xcc>
  402ce2:       e8 69 e0 ff ff          callq  400d50 <gethostbyname@plt>
  402ce7:       48 85 c0                test   %rax,%rax
  402cea:       75 68                   jne    402d54 <init_driver+0x12a>
  402cec:       48 b8 45 72 72 6f 72    movabs $0x44203a726f727245,%rax
  402cf3:       3a 20 44
  402cf6:       48 89 45 00             mov    %rax,0x0(%rbp)
  402cfa:       48 b8 4e 53 20 69 73    movabs $0x6e7520736920534e,%rax
  402d01:       20 75 6e
  402d04:       48 89 45 08             mov    %rax,0x8(%rbp)
  402d08:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402d0f:       74 6f 20
  402d12:       48 89 45 10             mov    %rax,0x10(%rbp)
  402d16:       48 b8 72 65 73 6f 6c    movabs $0x2065766c6f736572,%rax
  402d1d:       76 65 20
  402d20:       48 89 45 18             mov    %rax,0x18(%rbp)
  402d24:       48 b8 73 65 72 76 65    movabs $0x6120726576726573,%rax
  402d2b:       72 20 61
  402d2e:       48 89 45 20             mov    %rax,0x20(%rbp)
  402d32:       c7 45 28 64 64 72 65    movl   $0x65726464,0x28(%rbp)
  402d39:       66 c7 45 2c 73 73       movw   $0x7373,0x2c(%rbp)
  402d3f:       c6 45 2e 00             movb   $0x0,0x2e(%rbp)
  402d43:       89 df                   mov    %ebx,%edi
  402d45:       e8 d6 df ff ff          callq  400d20 <close@plt>
  402d4a:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402d4f:       e9 b1 00 00 00          jmpq   402e05 <init_driver+0x1db>
  402d54:       48 c7 04 24 00 00 00    movq   $0x0,(%rsp)
  402d5b:       00
  402d5c:       48 c7 44 24 08 00 00    movq   $0x0,0x8(%rsp)
  402d63:       00 00
  402d65:       66 c7 04 24 02 00       movw   $0x2,(%rsp)
  402d6b:       48 63 50 14             movslq 0x14(%rax),%rdx
  402d6f:       48 8b 40 18             mov    0x18(%rax),%rax
  402d73:       48 8b 30                mov    (%rax),%rsi
  402d76:       48 8d 7c 24 04          lea    0x4(%rsp),%rdi
  402d7b:       b9 0c 00 00 00          mov    $0xc,%ecx
  402d80:       e8 db df ff ff          callq  400d60 <__memmove_chk@plt>
  402d85:       66 c7 44 24 02 4b 79    movw   $0x794b,0x2(%rsp)
  402d8c:       ba 10 00 00 00          mov    $0x10,%edx
  402d91:       48 89 e6                mov    %rsp,%rsi
  402d94:       89 df                   mov    %ebx,%edi
  402d96:       e8 a5 e0 ff ff          callq  400e40 <connect@plt>
  402d9b:       85 c0                   test   %eax,%eax
  402d9d:       79 50                   jns    402def <init_driver+0x1c5>
  402d9f:       48 b8 45 72 72 6f 72    movabs $0x55203a726f727245,%rax
  402da6:       3a 20 55
  402da9:       48 89 45 00             mov    %rax,0x0(%rbp)
  402dad:       48 b8 6e 61 62 6c 65    movabs $0x6f7420656c62616e,%rax
  402db4:       20 74 6f
  402db7:       48 89 45 08             mov    %rax,0x8(%rbp)
  402dbb:       48 b8 20 63 6f 6e 6e    movabs $0x7463656e6e6f6320,%rax
  402dc2:       65 63 74
  402dc5:       48 89 45 10             mov    %rax,0x10(%rbp)
  402dc9:       48 b8 20 74 6f 20 73    movabs $0x76726573206f7420,%rax
  402dd0:       65 72 76
  402dd3:       48 89 45 18             mov    %rax,0x18(%rbp)
  402dd7:       66 c7 45 20 65 72       movw   $0x7265,0x20(%rbp)
  402ddd:       c6 45 22 00             movb   $0x0,0x22(%rbp)
  402de1:       89 df                   mov    %ebx,%edi
  402de3:       e8 38 df ff ff          callq  400d20 <close@plt>
  402de8:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402ded:       eb 16                   jmp    402e05 <init_driver+0x1db>
  402def:       89 df                   mov    %ebx,%edi
  402df1:       e8 2a df ff ff          callq  400d20 <close@plt>
  402df6:       66 c7 45 00 4f 4b       movw   $0x4b4f,0x0(%rbp)
  402dfc:       c6 45 02 00             movb   $0x0,0x2(%rbp)
  402e00:       b8 00 00 00 00          mov    $0x0,%eax
  402e05:       48 8b 4c 24 18          mov    0x18(%rsp),%rcx
  402e0a:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
  402e11:       00 00
  402e13:       74 05                   je     402e1a <init_driver+0x1f0>
  402e15:       e8 c6 de ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402e1a:       48 83 c4 20             add    $0x20,%rsp
  402e1e:       5b                      pop    %rbx
  402e1f:       5d                      pop    %rbp
  402e20:       41 5c                   pop    %r12
  402e22:       c3                      retq

0000000000402e23 <driver_post>:
  402e23:       53                      push   %rbx
  402e24:       4c 89 cb                mov    %r9,%rbx
  402e27:       45 85 c0                test   %r8d,%r8d
  402e2a:       74 29                   je     402e55 <driver_post+0x32>
  402e2c:       48 89 ca                mov    %rcx,%rdx
  402e2f:       48 8d 35 15 09 00 00    lea    0x915(%rip),%rsi        # 40374b <trans_char+0xdb>
  402e36:       bf 01 00 00 00          mov    $0x1,%edi
  402e3b:       b8 00 00 00 00          mov    $0x0,%eax
  402e40:       e8 9b df ff ff          callq  400de0 <__printf_chk@plt>
  402e45:       66 c7 03 4f 4b          movw   $0x4b4f,(%rbx)
  402e4a:       c6 43 02 00             movb   $0x0,0x2(%rbx)
  402e4e:       b8 00 00 00 00          mov    $0x0,%eax
  402e53:       eb 41                   jmp    402e96 <driver_post+0x73>
  402e55:       48 85 ff                test   %rdi,%rdi
  402e58:       74 2e                   je     402e88 <driver_post+0x65>
  402e5a:       80 3f 00                cmpb   $0x0,(%rdi)
  402e5d:       74 29                   je     402e88 <driver_post+0x65>
  402e5f:       48 83 ec 08             sub    $0x8,%rsp
  402e63:       41 51                   push   %r9
  402e65:       49 89 c9                mov    %rcx,%r9
  402e68:       49 89 d0                mov    %rdx,%r8
  402e6b:       48 89 f9                mov    %rdi,%rcx
  402e6e:       48 89 f2                mov    %rsi,%rdx
  402e71:       be 79 4b 00 00          mov    $0x4b79,%esi
  402e76:       48 8d 3d bf 08 00 00    lea    0x8bf(%rip),%rdi        # 40373c <trans_char+0xcc>
  402e7d:       e8 2b f6 ff ff          callq  4024ad <submitr>
  402e82:       48 83 c4 10             add    $0x10,%rsp
  402e86:       eb 0e                   jmp    402e96 <driver_post+0x73>
  402e88:       66 c7 03 4f 4b          movw   $0x4b4f,(%rbx)
  402e8d:       c6 43 02 00             movb   $0x0,0x2(%rbx)
  402e91:       b8 00 00 00 00          mov    $0x0,%eax
  402e96:       5b                      pop    %rbx
  402e97:       c3                      retq

0000000000402e98 <check>:
  402e98:       89 f8                   mov    %edi,%eax
  402e9a:       c1 e8 1c                shr    $0x1c,%eax
  402e9d:       85 c0                   test   %eax,%eax
  402e9f:       74 1d                   je     402ebe <check+0x26>
  402ea1:       b9 00 00 00 00          mov    $0x0,%ecx
  402ea6:       eb 0b                   jmp    402eb3 <check+0x1b>
  402ea8:       89 f8                   mov    %edi,%eax
  402eaa:       d3 e8                   shr    %cl,%eax
  402eac:       3c 0a                   cmp    $0xa,%al
  402eae:       74 14                   je     402ec4 <check+0x2c>
  402eb0:       83 c1 08                add    $0x8,%ecx
  402eb3:       83 f9 1f                cmp    $0x1f,%ecx
  402eb6:       7e f0                   jle    402ea8 <check+0x10>
  402eb8:       b8 01 00 00 00          mov    $0x1,%eax
  402ebd:       c3                      retq
  402ebe:       b8 00 00 00 00          mov    $0x0,%eax
  402ec3:       c3                      retq
  402ec4:       b8 00 00 00 00          mov    $0x0,%eax
  402ec9:       c3                      retq

0000000000402eca <gencookie>:
  402eca:       53                      push   %rbx
  402ecb:       83 c7 01                add    $0x1,%edi
  402ece:       e8 bd dd ff ff          callq  400c90 <srandom@plt>
  402ed3:       e8 c8 de ff ff          callq  400da0 <random@plt>
  402ed8:       89 c3                   mov    %eax,%ebx
  402eda:       89 c7                   mov    %eax,%edi
  402edc:       e8 b7 ff ff ff          callq  402e98 <check>
  402ee1:       85 c0                   test   %eax,%eax
  402ee3:       74 ee                   je     402ed3 <gencookie+0x9>
  402ee5:       89 d8                   mov    %ebx,%eax
  402ee7:       5b                      pop    %rbx
  402ee8:       c3                      retq
  402ee9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000402ef0 <__libc_csu_init>:
  402ef0:       41 57                   push   %r15
  402ef2:       41 56                   push   %r14
  402ef4:       49 89 d7                mov    %rdx,%r15
  402ef7:       41 55                   push   %r13
  402ef9:       41 54                   push   %r12
  402efb:       4c 8d 25 06 1f 20 00    lea    0x201f06(%rip),%r12        # 604e08 <__frame_dummy_init_array_entry>
  402f02:       55                      push   %rbp
  402f03:       48 8d 2d 06 1f 20 00    lea    0x201f06(%rip),%rbp        # 604e10 <__init_array_end>
  402f0a:       53                      push   %rbx
  402f0b:       41 89 fd                mov    %edi,%r13d
  402f0e:       49 89 f6                mov    %rsi,%r14
  402f11:       4c 29 e5                sub    %r12,%rbp
  402f14:       48 83 ec 08             sub    $0x8,%rsp
  402f18:       48 c1 fd 03             sar    $0x3,%rbp
  402f1c:       e8 27 dd ff ff          callq  400c48 <_init>
  402f21:       48 85 ed                test   %rbp,%rbp
  402f24:       74 20                   je     402f46 <__libc_csu_init+0x56>
  402f26:       31 db                   xor    %ebx,%ebx
  402f28:       0f 1f 84 00 00 00 00    nopl   0x0(%rax,%rax,1)
  402f2f:       00
  402f30:       4c 89 fa                mov    %r15,%rdx
  402f33:       4c 89 f6                mov    %r14,%rsi
  402f36:       44 89 ef                mov    %r13d,%edi
  402f39:       41 ff 14 dc             callq  *(%r12,%rbx,8)
  402f3d:       48 83 c3 01             add    $0x1,%rbx
  402f41:       48 39 dd                cmp    %rbx,%rbp
  402f44:       75 ea                   jne    402f30 <__libc_csu_init+0x40>
  402f46:       48 83 c4 08             add    $0x8,%rsp
  402f4a:       5b                      pop    %rbx
  402f4b:       5d                      pop    %rbp
  402f4c:       41 5c                   pop    %r12
  402f4e:       41 5d                   pop    %r13
  402f50:       41 5e                   pop    %r14
  402f52:       41 5f                   pop    %r15
  402f54:       c3                      retq
  402f55:       90                      nop
  402f56:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  402f5d:       00 00 00

0000000000402f60 <__libc_csu_fini>:
  402f60:       f3 c3                   repz retq

Disassembly of section .fini:

0000000000402f64 <_fini>:
  402f64:       48 83 ec 08             sub    $0x8,%rsp
  402f68:       48 83 c4 08             add    $0x8,%rsp
  402f6c:       c3                      retq