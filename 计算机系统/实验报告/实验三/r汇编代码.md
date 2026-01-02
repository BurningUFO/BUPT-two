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
  400c70:       ff 25 a2 43 20 00       jmpq   *0x2043a2(%rip)        # 605018 <strcasecmp@GLIBC_2.2.5>
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
  400e8f:       49 c7 c0 80 30 40 00    mov    $0x403080,%r8
  400e96:       48 c7 c1 10 30 40 00    mov    $0x403010,%rcx
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
  400f96:       48 8d 35 fb 20 00 00    lea    0x20fb(%rip),%rsi        # 403098 <_IO_stdin_used+0x8>
  400f9d:       bf 01 00 00 00          mov    $0x1,%edi
  400fa2:       b8 00 00 00 00          mov    $0x0,%eax
  400fa7:       e8 34 fe ff ff          callq  400de0 <__printf_chk@plt>
  400fac:       48 8d 3d 1d 21 00 00    lea    0x211d(%rip),%rdi        # 4030d0 <_IO_stdin_used+0x40>
  400fb3:       e8 08 fd ff ff          callq  400cc0 <puts@plt>
  400fb8:       48 8d 3d 89 22 00 00    lea    0x2289(%rip),%rdi        # 403248 <_IO_stdin_used+0x1b8>
  400fbf:       e8 fc fc ff ff          callq  400cc0 <puts@plt>
  400fc4:       48 8d 3d 2d 21 00 00    lea    0x212d(%rip),%rdi        # 4030f8 <_IO_stdin_used+0x68>
  400fcb:       e8 f0 fc ff ff          callq  400cc0 <puts@plt>
  400fd0:       48 8d 3d 8b 22 00 00    lea    0x228b(%rip),%rdi        # 403262 <_IO_stdin_used+0x1d2>
  400fd7:       e8 e4 fc ff ff          callq  400cc0 <puts@plt>
  400fdc:       eb 3a                   jmp    401018 <usage+0x92>
  400fde:       48 8d 35 99 22 00 00    lea    0x2299(%rip),%rsi        # 40327e <_IO_stdin_used+0x1ee>
  400fe5:       bf 01 00 00 00          mov    $0x1,%edi
  400fea:       b8 00 00 00 00          mov    $0x0,%eax
  400fef:       e8 ec fd ff ff          callq  400de0 <__printf_chk@plt>
  400ff4:       48 8d 3d 25 21 00 00    lea    0x2125(%rip),%rdi        # 403120 <_IO_stdin_used+0x90>
  400ffb:       e8 c0 fc ff ff          callq  400cc0 <puts@plt>
  401000:       48 8d 3d 41 21 00 00    lea    0x2141(%rip),%rdi        # 403148 <_IO_stdin_used+0xb8>
  401007:       e8 b4 fc ff ff          callq  400cc0 <puts@plt>
  40100c:       48 8d 3d 89 22 00 00    lea    0x2289(%rip),%rdi        # 40329c <_IO_stdin_used+0x20c>
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
  40104c:       e8 92 1f 00 00          callq  402fe3 <gencookie>
  401051:       89 05 ad 44 20 00       mov    %eax,0x2044ad(%rip)        # 605504 <cookie>
  401057:       89 c7                   mov    %eax,%edi
  401059:       e8 85 1f 00 00          callq  402fe3 <gencookie>
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
  4010b6:       c6 05 6b 50 20 00 72    movb   $0x72,0x20506b(%rip)        # 606128 <target_prefix>
  4010bd:       83 3d c4 43 20 00 00    cmpl   $0x0,0x2043c4(%rip)        # 605488 <notify>
  4010c4:       0f 84 c4 00 00 00       je     40118e <initialize_target+0x16c>
  4010ca:       83 3d 37 44 20 00 00    cmpl   $0x0,0x204437(%rip)        # 605508 <is_checker>
  4010d1:       0f 85 b7 00 00 00       jne    40118e <initialize_target+0x16c>
  4010d7:       48 89 e7                mov    %rsp,%rdi
  4010da:       be 00 01 00 00          mov    $0x100,%esi
  4010df:       e8 3c fd ff ff          callq  400e20 <gethostname@plt>
  4010e4:       85 c0                   test   %eax,%eax
  4010e6:       74 27                   je     40110f <initialize_target+0xed>
  4010e8:       48 8d 3d 89 20 00 00    lea    0x2089(%rip),%rdi        # 403178 <_IO_stdin_used+0xe8>
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
  40113a:       48 8d 35 6f 20 00 00    lea    0x206f(%rip),%rsi        # 4031b0 <_IO_stdin_used+0x120>
  401141:       bf 01 00 00 00          mov    $0x1,%edi
  401146:       e8 95 fc ff ff          callq  400de0 <__printf_chk@plt>
  40114b:       bf 08 00 00 00          mov    $0x8,%edi
  401150:       e8 db fc ff ff          callq  400e30 <exit@plt>
  401155:       48 8d bc 24 00 01 00    lea    0x100(%rsp),%rdi
  40115c:       00
  40115d:       e8 e1 1b 00 00          callq  402d43 <init_driver>
  401162:       85 c0                   test   %eax,%eax
  401164:       79 28                   jns    40118e <initialize_target+0x16c>
  401166:       48 8d 94 24 00 01 00    lea    0x100(%rsp),%rdx
  40116d:       00
  40116e:       48 8d 35 7b 20 00 00    lea    0x207b(%rip),%rsi        # 4031f0 <_IO_stdin_used+0x160>
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
  4011be:       48 c7 c6 7e 20 40 00    mov    $0x40207e,%rsi
  4011c5:       bf 0b 00 00 00          mov    $0xb,%edi
  4011ca:       e8 71 fb ff ff          callq  400d40 <signal@plt>
  4011cf:       48 c7 c6 2a 20 40 00    mov    $0x40202a,%rsi
  4011d6:       bf 07 00 00 00          mov    $0x7,%edi
  4011db:       e8 60 fb ff ff          callq  400d40 <signal@plt>
  4011e0:       48 c7 c6 d2 20 40 00    mov    $0x4020d2,%rsi
  4011e7:       bf 04 00 00 00          mov    $0x4,%edi
  4011ec:       e8 4f fb ff ff          callq  400d40 <signal@plt>
  4011f1:       83 3d 10 43 20 00 00    cmpl   $0x0,0x204310(%rip)        # 605508 <is_checker>
  4011f8:       74 24                   je     40121e <main+0x6e>
  4011fa:       48 c7 c6 26 21 40 00    mov    $0x402126,%rsi
  401201:       bf 0e 00 00 00          mov    $0xe,%edi
  401206:       e8 35 fb ff ff          callq  400d40 <signal@plt>
  40120b:       bf 05 00 00 00          mov    $0x5,%edi
  401210:       e8 fb fa ff ff          callq  400d10 <alarm@plt>
  401215:       48 8d 2d 9e 20 00 00    lea    0x209e(%rip),%rbp        # 4032ba <_IO_stdin_used+0x22a>
  40121c:       eb 07                   jmp    401225 <main+0x75>
  40121e:       48 8d 2d 90 20 00 00    lea    0x2090(%rip),%rbp        # 4032b5 <_IO_stdin_used+0x225>
  401225:       48 8b 05 74 42 20 00    mov    0x204274(%rip),%rax        # 6054a0 <stdin@@GLIBC_2.2.5>
  40122c:       48 89 05 bd 42 20 00    mov    %rax,0x2042bd(%rip)        # 6054f0 <infile>
  401233:       41 bd 00 00 00 00       mov    $0x0,%r13d
  401239:       41 be 00 00 00 00       mov    $0x0,%r14d
  40123f:       e9 d5 00 00 00          jmpq   401319 <main+0x169>
  401244:       83 e8 61                sub    $0x61,%eax
  401247:       3c 10                   cmp    $0x10,%al
  401249:       0f 87 a9 00 00 00       ja     4012f8 <main+0x148>
  40124f:       0f b6 c0                movzbl %al,%eax
  401252:       48 8d 0d a7 20 00 00    lea    0x20a7(%rip),%rcx        # 403300 <_IO_stdin_used+0x270>
  401259:       48 63 04 81             movslq (%rcx,%rax,4),%rax
  40125d:       48 01 c1                add    %rax,%rcx
  401260:       ff e1                   jmpq   *%rcx
  401262:       48 8b 3b                mov    (%rbx),%rdi
  401265:       e8 1c fd ff ff          callq  400f86 <usage>
  40126a:       48 8d 35 dc 22 00 00    lea    0x22dc(%rip),%rsi        # 40354d <_IO_stdin_used+0x4bd>
  401271:       48 8b 3d 30 42 20 00    mov    0x204230(%rip),%rdi        # 6054a8 <optarg@@GLIBC_2.2.5>
  401278:       e8 73 fb ff ff          callq  400df0 <fopen@plt>
  40127d:       48 89 05 6c 42 20 00    mov    %rax,0x20426c(%rip)        # 6054f0 <infile>
  401284:       48 85 c0                test   %rax,%rax
  401287:       0f 85 8c 00 00 00       jne    401319 <main+0x169>
  40128d:       48 8b 0d 14 42 20 00    mov    0x204214(%rip),%rcx        # 6054a8 <optarg@@GLIBC_2.2.5>
  401294:       48 8d 15 27 20 00 00    lea    0x2027(%rip),%rdx        # 4032c2 <_IO_stdin_used+0x232>
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
  4012fb:       48 8d 35 dd 1f 00 00    lea    0x1fdd(%rip),%rsi        # 4032df <_IO_stdin_used+0x24f>
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
  401331:       be 01 00 00 00          mov    $0x1,%esi
  401336:       44 89 ef                mov    %r13d,%edi
  401339:       e8 e4 fc ff ff          callq  401022 <initialize_target>
  40133e:       83 3d c3 41 20 00 00    cmpl   $0x0,0x2041c3(%rip)        # 605508 <is_checker>
  401345:       74 2c                   je     401373 <main+0x1c3>
  401347:       44 3b 35 b2 41 20 00    cmp    0x2041b2(%rip),%r14d        # 605500 <authkey>
  40134e:       74 23                   je     401373 <main+0x1c3>
  401350:       44 89 f2                mov    %r14d,%edx
  401353:       48 8d 35 be 1e 00 00    lea    0x1ebe(%rip),%rsi        # 403218 <_IO_stdin_used+0x188>
  40135a:       bf 01 00 00 00          mov    $0x1,%edi
  40135f:       b8 00 00 00 00          mov    $0x0,%eax
  401364:       e8 77 fa ff ff          callq  400de0 <__printf_chk@plt>
  401369:       b8 00 00 00 00          mov    $0x0,%eax
  40136e:       e8 28 09 00 00          callq  401c9b <check_fail>
  401373:       8b 15 8b 41 20 00       mov    0x20418b(%rip),%edx        # 605504 <cookie>
  401379:       48 8d 35 72 1f 00 00    lea    0x1f72(%rip),%rsi        # 4032f2 <_IO_stdin_used+0x262>
  401380:       bf 01 00 00 00          mov    $0x1,%edi
  401385:       b8 00 00 00 00          mov    $0x0,%eax
  40138a:       e8 51 fa ff ff          callq  400de0 <__printf_chk@plt>
  40138f:       48 8b 3d ea 40 20 00    mov    0x2040ea(%rip),%rdi        # 605480 <buf_offset>
  401396:       e8 e2 0d 00 00          callq  40217d <launch>
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
  401909:       e8 c5 03 00 00          callq  401cd3 <Gets>
  40190e:       b8 01 00 00 00          mov    $0x1,%eax
  401913:       48 83 c4 18             add    $0x18,%rsp
  401917:       c3                      retq

0000000000401918 <touch1>:
  401918:       48 83 ec 08             sub    $0x8,%rsp
  40191c:       48 c1 ec 04             shr    $0x4,%rsp
  401920:       48 c1 e4 04             shl    $0x4,%rsp
  401924:       c7 05 ce 3b 20 00 01    movl   $0x1,0x203bce(%rip)        # 6054fc <vlevel>
  40192b:       00 00 00
  40192e:       48 8d 3d 6f 1a 00 00    lea    0x1a6f(%rip),%rdi        # 4033a4 <_IO_stdin_used+0x314>
  401935:       e8 86 f3 ff ff          callq  400cc0 <puts@plt>
  40193a:       bf 01 00 00 00          mov    $0x1,%edi
  40193f:       e8 f1 05 00 00          callq  401f35 <validate>
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
  40196e:       48 8d 35 53 1a 00 00    lea    0x1a53(%rip),%rsi        # 4033c8 <_IO_stdin_used+0x338>
  401975:       bf 01 00 00 00          mov    $0x1,%edi
  40197a:       b8 00 00 00 00          mov    $0x0,%eax
  40197f:       e8 5c f4 ff ff          callq  400de0 <__printf_chk@plt>
  401984:       bf 02 00 00 00          mov    $0x2,%edi
  401989:       e8 a7 05 00 00          callq  401f35 <validate>
  40198e:       eb 20                   jmp    4019b0 <touch2+0x62>
  401990:       48 8d 35 59 1a 00 00    lea    0x1a59(%rip),%rsi        # 4033f0 <_IO_stdin_used+0x360>
  401997:       bf 01 00 00 00          mov    $0x1,%edi
  40199c:       b8 00 00 00 00          mov    $0x0,%eax
  4019a1:       e8 3a f4 ff ff          callq  400de0 <__printf_chk@plt>
  4019a6:       bf 02 00 00 00          mov    $0x2,%edi
  4019ab:       e8 52 06 00 00          callq  402002 <fail>
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
  401a17:       48 8d 0d a3 19 00 00    lea    0x19a3(%rip),%rcx        # 4033c1 <_IO_stdin_used+0x331>
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
  401a98:       48 8d 35 79 19 00 00    lea    0x1979(%rip),%rsi        # 403418 <_IO_stdin_used+0x388>
  401a9f:       bf 01 00 00 00          mov    $0x1,%edi
  401aa4:       b8 00 00 00 00          mov    $0x0,%eax
  401aa9:       e8 32 f3 ff ff          callq  400de0 <__printf_chk@plt>
  401aae:       bf 03 00 00 00          mov    $0x3,%edi
  401ab3:       e8 7d 04 00 00          callq  401f35 <validate>
  401ab8:       eb 23                   jmp    401add <touch3+0x70>
  401aba:       48 89 da                mov    %rbx,%rdx
  401abd:       48 8d 35 7c 19 00 00    lea    0x197c(%rip),%rsi        # 403440 <_IO_stdin_used+0x3b0>
  401ac4:       bf 01 00 00 00          mov    $0x1,%edi
  401ac9:       b8 00 00 00 00          mov    $0x0,%eax
  401ace:       e8 0d f3 ff ff          callq  400de0 <__printf_chk@plt>
  401ad3:       bf 03 00 00 00          mov    $0x3,%edi
  401ad8:       e8 25 05 00 00          callq  402002 <fail>
  401add:       bf 00 00 00 00          mov    $0x0,%edi
  401ae2:       e8 49 f3 ff ff          callq  400e30 <exit@plt>

0000000000401ae7 <test>:
  401ae7:       48 83 ec 08             sub    $0x8,%rsp
  401aeb:       b8 00 00 00 00          mov    $0x0,%eax
  401af0:       e8 0d fe ff ff          callq  401902 <getbuf>
  401af5:       89 c2                   mov    %eax,%edx
  401af7:       48 8d 35 6a 19 00 00    lea    0x196a(%rip),%rsi        # 403468 <_IO_stdin_used+0x3d8>
  401afe:       bf 01 00 00 00          mov    $0x1,%edi
  401b03:       b8 00 00 00 00          mov    $0x0,%eax
  401b08:       e8 d3 f2 ff ff          callq  400de0 <__printf_chk@plt>
  401b0d:       48 83 c4 08             add    $0x8,%rsp
  401b11:       c3                      retq

0000000000401b12 <start_farm>:
  401b12:       b8 01 00 00 00          mov    $0x1,%eax
  401b17:       c3                      retq

0000000000401b18 <getval_492>:
  401b18:       b8 68 89 c7 90          mov    $0x90c78968,%eax
  401b1d:       c3                      retq

0000000000401b1e <setval_106>:
  401b1e:       c7 07 48 89 c7 92       movl   $0x92c78948,(%rdi)
  401b24:       c3                      retq

0000000000401b25 <getval_371>:
  401b25:       b8 0b 58 92 90          mov    $0x9092580b,%eax
  401b2a:       c3                      retq

0000000000401b2b <getval_146>:
  401b2b:       b8 9b 58 90 c3          mov    $0xc390589b,%eax
  401b30:       c3                      retq

0000000000401b31 <addval_322>:
  401b31:       8d 87 58 90 90 90       lea    -0x6f6f6fa8(%rdi),%eax
  401b37:       c3                      retq

0000000000401b38 <getval_209>:
  401b38:       b8 3b 48 89 c7          mov    $0xc789483b,%eax
  401b3d:       c3                      retq

0000000000401b3e <getval_124>:
  401b3e:       b8 48 89 c7 c3          mov    $0xc3c78948,%eax
  401b43:       c3                      retq

0000000000401b44 <getval_427>:
  401b44:       b8 58 94 90 90          mov    $0x90909458,%eax
  401b49:       c3                      retq

0000000000401b4a <mid_farm>:
  401b4a:       b8 01 00 00 00          mov    $0x1,%eax
  401b4f:       c3                      retq

0000000000401b50 <add_xy>:
  401b50:       48 8d 04 37             lea    (%rdi,%rsi,1),%rax
  401b54:       c3                      retq

0000000000401b55 <getval_105>:
  401b55:       b8 89 d6 92 90          mov    $0x9092d689,%eax
  401b5a:       c3                      retq

0000000000401b5b <addval_346>:
  401b5b:       8d 87 89 d6 a4 d2       lea    -0x2d5b2977(%rdi),%eax
  401b61:       c3                      retq

0000000000401b62 <getval_389>:
  401b62:       b8 48 99 e0 c3          mov    $0xc3e09948,%eax
  401b67:       c3                      retq

0000000000401b68 <addval_231>:
  401b68:       8d 87 89 ca 94 db       lea    -0x246b3577(%rdi),%eax
  401b6e:       c3                      retq

0000000000401b6f <setval_240>:
  401b6f:       c7 07 48 89 e0 91       movl   $0x91e08948,(%rdi)
  401b75:       c3                      retq

0000000000401b76 <getval_100>:
  401b76:       b8 89 d6 78 c0          mov    $0xc078d689,%eax
  401b7b:       c3                      retq

0000000000401b7c <addval_393>:
  401b7c:       8d 87 c9 ca 90 90       lea    -0x6f6f3537(%rdi),%eax
  401b82:       c3                      retq

0000000000401b83 <getval_254>:
  401b83:       b8 5f 89 ca 90          mov    $0x90ca895f,%eax
  401b88:       c3                      retq

0000000000401b89 <getval_447>:
  401b89:       b8 48 89 e0 92          mov    $0x92e08948,%eax
  401b8e:       c3                      retq

0000000000401b8f <getval_165>:
  401b8f:       b8 89 c1 c1 aa          mov    $0xaac1c189,%eax
  401b94:       c3                      retq

0000000000401b95 <addval_420>:
  401b95:       8d 87 99 ca 84 c9       lea    -0x367b3567(%rdi),%eax
  401b9b:       c3                      retq

0000000000401b9c <addval_156>:
  401b9c:       8d 87 81 ca 90 90       lea    -0x6f6f357f(%rdi),%eax
  401ba2:       c3                      retq

0000000000401ba3 <getval_362>:
  401ba3:       b8 89 c1 60 d2          mov    $0xd260c189,%eax
  401ba8:       c3                      retq

0000000000401ba9 <getval_317>:
  401ba9:       b8 d7 89 ca 90          mov    $0x90ca89d7,%eax
  401bae:       c3                      retq

0000000000401baf <setval_411>:
  401baf:       c7 07 89 c1 91 c3       movl   $0xc391c189,(%rdi)
  401bb5:       c3                      retq

0000000000401bb6 <getval_391>:
  401bb6:       b8 8d d6 c3 97          mov    $0x97c3d68d,%eax
  401bbb:       c3                      retq

0000000000401bbc <getval_426>:
  401bbc:       b8 48 89 e0 91          mov    $0x91e08948,%eax
  401bc1:       c3                      retq

0000000000401bc2 <setval_466>:
  401bc2:       c7 07 f4 89 c1 94       movl   $0x94c189f4,(%rdi)
  401bc8:       c3                      retq

0000000000401bc9 <setval_235>:
  401bc9:       c7 07 c9 d6 20 db       movl   $0xdb20d6c9,(%rdi)
  401bcf:       c3                      retq

0000000000401bd0 <getval_110>:
  401bd0:       b8 76 89 c1 c1          mov    $0xc1c18976,%eax
  401bd5:       c3                      retq

0000000000401bd6 <getval_456>:
  401bd6:       b8 ae 9e 88 ca          mov    $0xca889eae,%eax
  401bdb:       c3                      retq

0000000000401bdc <getval_459>:
  401bdc:       b8 48 a9 e0 c3          mov    $0xc3e0a948,%eax
  401be1:       c3                      retq

0000000000401be2 <setval_183>:
  401be2:       c7 07 89 d6 90 90       movl   $0x9090d689,(%rdi)
  401be8:       c3                      retq

0000000000401be9 <setval_338>:
  401be9:       c7 07 89 c1 c3 bf       movl   $0xbfc3c189,(%rdi)
  401bef:       c3                      retq

0000000000401bf0 <addval_139>:
  401bf0:       8d 87 a9 ca 90 c3       lea    -0x3c6f3557(%rdi),%eax
  401bf6:       c3                      retq

0000000000401bf7 <getval_245>:
  401bf7:       b8 48 89 e0 c3          mov    $0xc3e08948,%eax
  401bfc:       c3                      retq

0000000000401bfd <setval_262>:
  401bfd:       c7 07 f2 48 89 e0       movl   $0xe08948f2,(%rdi)
  401c03:       c3                      retq

0000000000401c04 <setval_433>:
  401c04:       c7 07 99 c1 90 c3       movl   $0xc390c199,(%rdi)
  401c0a:       c3                      retq

0000000000401c0b <getval_339>:
  401c0b:       b8 48 89 e0 91          mov    $0x91e08948,%eax
  401c10:       c3                      retq

0000000000401c11 <setval_364>:
  401c11:       c7 07 09 d6 38 db       movl   $0xdb38d609,(%rdi)
  401c17:       c3                      retq

0000000000401c18 <getval_164>:
  401c18:       b8 86 89 c1 c3          mov    $0xc3c18986,%eax
  401c1d:       c3                      retq

0000000000401c1e <setval_224>:
  401c1e:       c7 07 89 d6 90 90       movl   $0x9090d689,(%rdi)
  401c24:       c3                      retq

0000000000401c25 <end_farm>:
  401c25:       b8 01 00 00 00          mov    $0x1,%eax
  401c2a:       c3                      retq

0000000000401c2b <save_char>:
  401c2b:       8b 05 f3 44 20 00       mov    0x2044f3(%rip),%eax        # 606124 <gets_cnt>
  401c31:       3d ff 03 00 00          cmp    $0x3ff,%eax
  401c36:       7f 4a                   jg     401c82 <save_char+0x57>
  401c38:       8d 14 40                lea    (%rax,%rax,2),%edx
  401c3b:       89 f9                   mov    %edi,%ecx
  401c3d:       c0 e9 04                shr    $0x4,%cl
  401c40:       4c 8d 05 49 1b 00 00    lea    0x1b49(%rip),%r8        # 403790 <trans_char>
  401c47:       83 e1 0f                and    $0xf,%ecx
  401c4a:       45 0f b6 0c 08          movzbl (%r8,%rcx,1),%r9d
  401c4f:       48 8d 0d ca 38 20 00    lea    0x2038ca(%rip),%rcx        # 605520 <gets_buf>
  401c56:       48 63 f2                movslq %edx,%rsi
  401c59:       44 88 0c 31             mov    %r9b,(%rcx,%rsi,1)
  401c5d:       8d 72 01                lea    0x1(%rdx),%esi
  401c60:       83 e7 0f                and    $0xf,%edi
  401c63:       41 0f b6 3c 38          movzbl (%r8,%rdi,1),%edi
  401c68:       48 63 f6                movslq %esi,%rsi
  401c6b:       40 88 3c 31             mov    %dil,(%rcx,%rsi,1)
  401c6f:       83 c2 02                add    $0x2,%edx
  401c72:       48 63 d2                movslq %edx,%rdx
  401c75:       c6 04 11 20             movb   $0x20,(%rcx,%rdx,1)
  401c79:       83 c0 01                add    $0x1,%eax
  401c7c:       89 05 a2 44 20 00       mov    %eax,0x2044a2(%rip)        # 606124 <gets_cnt>
  401c82:       f3 c3                   repz retq

0000000000401c84 <save_term>:
  401c84:       8b 05 9a 44 20 00       mov    0x20449a(%rip),%eax        # 606124 <gets_cnt>
  401c8a:       8d 04 40                lea    (%rax,%rax,2),%eax
  401c8d:       48 98                   cltq
  401c8f:       48 8d 15 8a 38 20 00    lea    0x20388a(%rip),%rdx        # 605520 <gets_buf>
  401c96:       c6 04 02 00             movb   $0x0,(%rdx,%rax,1)
  401c9a:       c3                      retq

0000000000401c9b <check_fail>:
  401c9b:       48 83 ec 08             sub    $0x8,%rsp
  401c9f:       0f be 15 82 44 20 00    movsbl 0x204482(%rip),%edx        # 606128 <target_prefix>
  401ca6:       4c 8d 05 73 38 20 00    lea    0x203873(%rip),%r8        # 605520 <gets_buf>
  401cad:       8b 0d 45 38 20 00       mov    0x203845(%rip),%ecx        # 6054f8 <check_level>
  401cb3:       48 8d 35 d1 17 00 00    lea    0x17d1(%rip),%rsi        # 40348b <_IO_stdin_used+0x3fb>
  401cba:       bf 01 00 00 00          mov    $0x1,%edi
  401cbf:       b8 00 00 00 00          mov    $0x0,%eax
  401cc4:       e8 17 f1 ff ff          callq  400de0 <__printf_chk@plt>
  401cc9:       bf 01 00 00 00          mov    $0x1,%edi
  401cce:       e8 5d f1 ff ff          callq  400e30 <exit@plt>

0000000000401cd3 <Gets>:
  401cd3:       41 54                   push   %r12
  401cd5:       55                      push   %rbp
  401cd6:       53                      push   %rbx
  401cd7:       49 89 fc                mov    %rdi,%r12
  401cda:       c7 05 40 44 20 00 00    movl   $0x0,0x204440(%rip)        # 606124 <gets_cnt>
  401ce1:       00 00 00
  401ce4:       48 89 fb                mov    %rdi,%rbx
  401ce7:       eb 11                   jmp    401cfa <Gets+0x27>
  401ce9:       48 8d 6b 01             lea    0x1(%rbx),%rbp
  401ced:       88 03                   mov    %al,(%rbx)
  401cef:       0f b6 f8                movzbl %al,%edi
  401cf2:       e8 34 ff ff ff          callq  401c2b <save_char>
  401cf7:       48 89 eb                mov    %rbp,%rbx
  401cfa:       48 8b 3d ef 37 20 00    mov    0x2037ef(%rip),%rdi        # 6054f0 <infile>
  401d01:       e8 aa f0 ff ff          callq  400db0 <_IO_getc@plt>
  401d06:       83 f8 ff                cmp    $0xffffffff,%eax
  401d09:       74 05                   je     401d10 <Gets+0x3d>
  401d0b:       83 f8 0a                cmp    $0xa,%eax
  401d0e:       75 d9                   jne    401ce9 <Gets+0x16>
  401d10:       c6 03 00                movb   $0x0,(%rbx)
  401d13:       b8 00 00 00 00          mov    $0x0,%eax
  401d18:       e8 67 ff ff ff          callq  401c84 <save_term>
  401d1d:       4c 89 e0                mov    %r12,%rax
  401d20:       5b                      pop    %rbx
  401d21:       5d                      pop    %rbp
  401d22:       41 5c                   pop    %r12
  401d24:       c3                      retq

0000000000401d25 <notify_server>:
  401d25:       53                      push   %rbx
  401d26:       48 81 ec 10 40 00 00    sub    $0x4010,%rsp
  401d2d:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  401d34:       00 00
  401d36:       48 89 84 24 08 40 00    mov    %rax,0x4008(%rsp)
  401d3d:       00
  401d3e:       31 c0                   xor    %eax,%eax
  401d40:       83 3d c1 37 20 00 00    cmpl   $0x0,0x2037c1(%rip)        # 605508 <is_checker>
  401d47:       0f 85 c7 01 00 00       jne    401f14 <notify_server+0x1ef>
  401d4d:       89 fb                   mov    %edi,%ebx
  401d4f:       8b 05 cf 43 20 00       mov    0x2043cf(%rip),%eax        # 606124 <gets_cnt>
  401d55:       83 c0 64                add    $0x64,%eax
  401d58:       3d 00 20 00 00          cmp    $0x2000,%eax
  401d5d:       7e 20                   jle    401d7f <notify_server+0x5a>
  401d5f:       48 8d 35 5a 18 00 00    lea    0x185a(%rip),%rsi        # 4035c0 <_IO_stdin_used+0x530>
  401d66:       bf 01 00 00 00          mov    $0x1,%edi
  401d6b:       b8 00 00 00 00          mov    $0x0,%eax
  401d70:       e8 6b f0 ff ff          callq  400de0 <__printf_chk@plt>
  401d75:       bf 01 00 00 00          mov    $0x1,%edi
  401d7a:       e8 b1 f0 ff ff          callq  400e30 <exit@plt>
  401d7f:       0f be 05 a2 43 20 00    movsbl 0x2043a2(%rip),%eax        # 606128 <target_prefix>
  401d86:       83 3d fb 36 20 00 00    cmpl   $0x0,0x2036fb(%rip)        # 605488 <notify>
  401d8d:       74 08                   je     401d97 <notify_server+0x72>
  401d8f:       8b 15 6b 37 20 00       mov    0x20376b(%rip),%edx        # 605500 <authkey>
  401d95:       eb 05                   jmp    401d9c <notify_server+0x77>
  401d97:       ba ff ff ff ff          mov    $0xffffffff,%edx
  401d9c:       85 db                   test   %ebx,%ebx
  401d9e:       74 09                   je     401da9 <notify_server+0x84>
  401da0:       4c 8d 0d fa 16 00 00    lea    0x16fa(%rip),%r9        # 4034a1 <_IO_stdin_used+0x411>
  401da7:       eb 07                   jmp    401db0 <notify_server+0x8b>
  401da9:       4c 8d 0d f6 16 00 00    lea    0x16f6(%rip),%r9        # 4034a6 <_IO_stdin_used+0x416>
  401db0:       48 89 e7                mov    %rsp,%rdi
  401db3:       48 8d 0d 66 37 20 00    lea    0x203766(%rip),%rcx        # 605520 <gets_buf>
  401dba:       51                      push   %rcx
  401dbb:       56                      push   %rsi
  401dbc:       50                      push   %rax
  401dbd:       52                      push   %rdx
  401dbe:       44 8b 05 6b 33 20 00    mov    0x20336b(%rip),%r8d        # 605130 <target_id>
  401dc5:       48 8d 0d df 16 00 00    lea    0x16df(%rip),%rcx        # 4034ab <_IO_stdin_used+0x41b>
  401dcc:       ba 00 20 00 00          mov    $0x2000,%edx
  401dd1:       be 01 00 00 00          mov    $0x1,%esi
  401dd6:       b8 00 00 00 00          mov    $0x0,%eax
  401ddb:       e8 80 f0 ff ff          callq  400e60 <__sprintf_chk@plt>
  401de0:       48 83 c4 20             add    $0x20,%rsp
  401de4:       83 3d 9d 36 20 00 00    cmpl   $0x0,0x20369d(%rip)        # 605488 <notify>
  401deb:       0f 84 89 00 00 00       je     401e7a <notify_server+0x155>
  401df1:       85 db                   test   %ebx,%ebx
  401df3:       74 74                   je     401e69 <notify_server+0x144>
  401df5:       48 89 e1                mov    %rsp,%rcx
  401df8:       4c 8d 8c 24 00 20 00    lea    0x2000(%rsp),%r9
  401dff:       00
  401e00:       41 b8 00 00 00 00       mov    $0x0,%r8d
  401e06:       48 8b 15 3b 33 20 00    mov    0x20333b(%rip),%rdx        # 605148 <lab>
  401e0d:       48 8b 35 3c 33 20 00    mov    0x20333c(%rip),%rsi        # 605150 <course>
  401e14:       48 8b 3d 25 33 20 00    mov    0x203325(%rip),%rdi        # 605140 <user_id>
  401e1b:       e8 1c 11 00 00          callq  402f3c <driver_post>
  401e20:       85 c0                   test   %eax,%eax
  401e22:       79 28                   jns    401e4c <notify_server+0x127>
  401e24:       48 8d 94 24 00 20 00    lea    0x2000(%rsp),%rdx
  401e2b:       00
  401e2c:       48 8d 35 94 16 00 00    lea    0x1694(%rip),%rsi        # 4034c7 <_IO_stdin_used+0x437>
  401e33:       bf 01 00 00 00          mov    $0x1,%edi
  401e38:       b8 00 00 00 00          mov    $0x0,%eax
  401e3d:       e8 9e ef ff ff          callq  400de0 <__printf_chk@plt>
  401e42:       bf 01 00 00 00          mov    $0x1,%edi
  401e47:       e8 e4 ef ff ff          callq  400e30 <exit@plt>
  401e4c:       48 8d 3d 9d 17 00 00    lea    0x179d(%rip),%rdi        # 4035f0 <_IO_stdin_used+0x560>
  401e53:       e8 68 ee ff ff          callq  400cc0 <puts@plt>
  401e58:       48 8d 3d 74 16 00 00    lea    0x1674(%rip),%rdi        # 4034d3 <_IO_stdin_used+0x443>
  401e5f:       e8 5c ee ff ff          callq  400cc0 <puts@plt>
  401e64:       e9 ab 00 00 00          jmpq   401f14 <notify_server+0x1ef>
  401e69:       48 8d 3d 6d 16 00 00    lea    0x166d(%rip),%rdi        # 4034dd <_IO_stdin_used+0x44d>
  401e70:       e8 4b ee ff ff          callq  400cc0 <puts@plt>
  401e75:       e9 9a 00 00 00          jmpq   401f14 <notify_server+0x1ef>
  401e7a:       85 db                   test   %ebx,%ebx
  401e7c:       74 09                   je     401e87 <notify_server+0x162>
  401e7e:       48 8d 15 1c 16 00 00    lea    0x161c(%rip),%rdx        # 4034a1 <_IO_stdin_used+0x411>
  401e85:       eb 07                   jmp    401e8e <notify_server+0x169>
  401e87:       48 8d 15 18 16 00 00    lea    0x1618(%rip),%rdx        # 4034a6 <_IO_stdin_used+0x416>
  401e8e:       48 8d 35 93 17 00 00    lea    0x1793(%rip),%rsi        # 403628 <_IO_stdin_used+0x598>
  401e95:       bf 01 00 00 00          mov    $0x1,%edi
  401e9a:       b8 00 00 00 00          mov    $0x0,%eax
  401e9f:       e8 3c ef ff ff          callq  400de0 <__printf_chk@plt>
  401ea4:       48 8b 15 95 32 20 00    mov    0x203295(%rip),%rdx        # 605140 <user_id>
  401eab:       48 8d 35 32 16 00 00    lea    0x1632(%rip),%rsi        # 4034e4 <_IO_stdin_used+0x454>
  401eb2:       bf 01 00 00 00          mov    $0x1,%edi
  401eb7:       b8 00 00 00 00          mov    $0x0,%eax
  401ebc:       e8 1f ef ff ff          callq  400de0 <__printf_chk@plt>
  401ec1:       48 8b 15 88 32 20 00    mov    0x203288(%rip),%rdx        # 605150 <course>
  401ec8:       48 8d 35 22 16 00 00    lea    0x1622(%rip),%rsi        # 4034f1 <_IO_stdin_used+0x461>
  401ecf:       bf 01 00 00 00          mov    $0x1,%edi
  401ed4:       b8 00 00 00 00          mov    $0x0,%eax
  401ed9:       e8 02 ef ff ff          callq  400de0 <__printf_chk@plt>
  401ede:       48 8b 15 63 32 20 00    mov    0x203263(%rip),%rdx        # 605148 <lab>
  401ee5:       48 8d 35 11 16 00 00    lea    0x1611(%rip),%rsi        # 4034fd <_IO_stdin_used+0x46d>
  401eec:       bf 01 00 00 00          mov    $0x1,%edi
  401ef1:       b8 00 00 00 00          mov    $0x0,%eax
  401ef6:       e8 e5 ee ff ff          callq  400de0 <__printf_chk@plt>
  401efb:       48 89 e2                mov    %rsp,%rdx
  401efe:       48 8d 35 01 16 00 00    lea    0x1601(%rip),%rsi        # 403506 <_IO_stdin_used+0x476>
  401f05:       bf 01 00 00 00          mov    $0x1,%edi
  401f0a:       b8 00 00 00 00          mov    $0x0,%eax
  401f0f:       e8 cc ee ff ff          callq  400de0 <__printf_chk@plt>
  401f14:       48 8b 84 24 08 40 00    mov    0x4008(%rsp),%rax
  401f1b:       00
  401f1c:       64 48 33 04 25 28 00    xor    %fs:0x28,%rax
  401f23:       00 00
  401f25:       74 05                   je     401f2c <notify_server+0x207>
  401f27:       e8 b4 ed ff ff          callq  400ce0 <__stack_chk_fail@plt>
  401f2c:       48 81 c4 10 40 00 00    add    $0x4010,%rsp
  401f33:       5b                      pop    %rbx
  401f34:       c3                      retq

0000000000401f35 <validate>:
  401f35:       53                      push   %rbx
  401f36:       89 fb                   mov    %edi,%ebx
  401f38:       83 3d c9 35 20 00 00    cmpl   $0x0,0x2035c9(%rip)        # 605508 <is_checker>
  401f3f:       74 72                   je     401fb3 <validate+0x7e>
  401f41:       39 3d b5 35 20 00       cmp    %edi,0x2035b5(%rip)        # 6054fc <vlevel>
  401f47:       74 16                   je     401f5f <validate+0x2a>
  401f49:       48 8d 3d c2 15 00 00    lea    0x15c2(%rip),%rdi        # 403512 <_IO_stdin_used+0x482>
  401f50:       e8 6b ed ff ff          callq  400cc0 <puts@plt>
  401f55:       b8 00 00 00 00          mov    $0x0,%eax
  401f5a:       e8 3c fd ff ff          callq  401c9b <check_fail>
  401f5f:       8b 15 93 35 20 00       mov    0x203593(%rip),%edx        # 6054f8 <check_level>
  401f65:       39 d7                   cmp    %edx,%edi
  401f67:       74 22                   je     401f8b <validate+0x56>
  401f69:       89 f9                   mov    %edi,%ecx
  401f6b:       48 8d 35 de 16 00 00    lea    0x16de(%rip),%rsi        # 403650 <_IO_stdin_used+0x5c0>
  401f72:       bf 01 00 00 00          mov    $0x1,%edi
  401f77:       b8 00 00 00 00          mov    $0x0,%eax
  401f7c:       e8 5f ee ff ff          callq  400de0 <__printf_chk@plt>
  401f81:       b8 00 00 00 00          mov    $0x0,%eax
  401f86:       e8 10 fd ff ff          callq  401c9b <check_fail>
  401f8b:       0f be 15 96 41 20 00    movsbl 0x204196(%rip),%edx        # 606128 <target_prefix>
  401f92:       4c 8d 05 87 35 20 00    lea    0x203587(%rip),%r8        # 605520 <gets_buf>
  401f99:       89 f9                   mov    %edi,%ecx
  401f9b:       48 8d 35 8e 15 00 00    lea    0x158e(%rip),%rsi        # 403530 <_IO_stdin_used+0x4a0>
  401fa2:       bf 01 00 00 00          mov    $0x1,%edi
  401fa7:       b8 00 00 00 00          mov    $0x0,%eax
  401fac:       e8 2f ee ff ff          callq  400de0 <__printf_chk@plt>
  401fb1:       eb 4d                   jmp    402000 <validate+0xcb>
  401fb3:       3b 3d 43 35 20 00       cmp    0x203543(%rip),%edi        # 6054fc <vlevel>
  401fb9:       74 1a                   je     401fd5 <validate+0xa0>
  401fbb:       48 8d 3d 50 15 00 00    lea    0x1550(%rip),%rdi        # 403512 <_IO_stdin_used+0x482>
  401fc2:       e8 f9 ec ff ff          callq  400cc0 <puts@plt>
  401fc7:       89 de                   mov    %ebx,%esi
  401fc9:       bf 00 00 00 00          mov    $0x0,%edi
  401fce:       e8 52 fd ff ff          callq  401d25 <notify_server>
  401fd3:       eb 2b                   jmp    402000 <validate+0xcb>
  401fd5:       0f be 0d 4c 41 20 00    movsbl 0x20414c(%rip),%ecx        # 606128 <target_prefix>
  401fdc:       89 fa                   mov    %edi,%edx
  401fde:       48 8d 35 93 16 00 00    lea    0x1693(%rip),%rsi        # 403678 <_IO_stdin_used+0x5e8>
  401fe5:       bf 01 00 00 00          mov    $0x1,%edi
  401fea:       b8 00 00 00 00          mov    $0x0,%eax
  401fef:       e8 ec ed ff ff          callq  400de0 <__printf_chk@plt>
  401ff4:       89 de                   mov    %ebx,%esi
  401ff6:       bf 01 00 00 00          mov    $0x1,%edi
  401ffb:       e8 25 fd ff ff          callq  401d25 <notify_server>
  402000:       5b                      pop    %rbx
  402001:       c3                      retq

0000000000402002 <fail>:
  402002:       48 83 ec 08             sub    $0x8,%rsp
  402006:       83 3d fb 34 20 00 00    cmpl   $0x0,0x2034fb(%rip)        # 605508 <is_checker>
  40200d:       74 0a                   je     402019 <fail+0x17>
  40200f:       b8 00 00 00 00          mov    $0x0,%eax
  402014:       e8 82 fc ff ff          callq  401c9b <check_fail>
  402019:       89 fe                   mov    %edi,%esi
  40201b:       bf 00 00 00 00          mov    $0x0,%edi
  402020:       e8 00 fd ff ff          callq  401d25 <notify_server>
  402025:       48 83 c4 08             add    $0x8,%rsp
  402029:       c3                      retq

000000000040202a <bushandler>:
  40202a:       48 83 ec 08             sub    $0x8,%rsp
  40202e:       83 3d d3 34 20 00 00    cmpl   $0x0,0x2034d3(%rip)        # 605508 <is_checker>
  402035:       74 16                   je     40204d <bushandler+0x23>
  402037:       48 8d 3d 07 15 00 00    lea    0x1507(%rip),%rdi        # 403545 <_IO_stdin_used+0x4b5>
  40203e:       e8 7d ec ff ff          callq  400cc0 <puts@plt>
  402043:       b8 00 00 00 00          mov    $0x0,%eax
  402048:       e8 4e fc ff ff          callq  401c9b <check_fail>
  40204d:       48 8d 3d 5c 16 00 00    lea    0x165c(%rip),%rdi        # 4036b0 <_IO_stdin_used+0x620>
  402054:       e8 67 ec ff ff          callq  400cc0 <puts@plt>
  402059:       48 8d 3d ef 14 00 00    lea    0x14ef(%rip),%rdi        # 40354f <_IO_stdin_used+0x4bf>
  402060:       e8 5b ec ff ff          callq  400cc0 <puts@plt>
  402065:       be 00 00 00 00          mov    $0x0,%esi
  40206a:       bf 00 00 00 00          mov    $0x0,%edi
  40206f:       e8 b1 fc ff ff          callq  401d25 <notify_server>
  402074:       bf 01 00 00 00          mov    $0x1,%edi
  402079:       e8 b2 ed ff ff          callq  400e30 <exit@plt>

000000000040207e <seghandler>:
  40207e:       48 83 ec 08             sub    $0x8,%rsp
  402082:       83 3d 7f 34 20 00 00    cmpl   $0x0,0x20347f(%rip)        # 605508 <is_checker>
  402089:       74 16                   je     4020a1 <seghandler+0x23>
  40208b:       48 8d 3d d3 14 00 00    lea    0x14d3(%rip),%rdi        # 403565 <_IO_stdin_used+0x4d5>
  402092:       e8 29 ec ff ff          callq  400cc0 <puts@plt>
  402097:       b8 00 00 00 00          mov    $0x0,%eax
  40209c:       e8 fa fb ff ff          callq  401c9b <check_fail>
  4020a1:       48 8d 3d 28 16 00 00    lea    0x1628(%rip),%rdi        # 4036d0 <_IO_stdin_used+0x640>
  4020a8:       e8 13 ec ff ff          callq  400cc0 <puts@plt>
  4020ad:       48 8d 3d 9b 14 00 00    lea    0x149b(%rip),%rdi        # 40354f <_IO_stdin_used+0x4bf>
  4020b4:       e8 07 ec ff ff          callq  400cc0 <puts@plt>
  4020b9:       be 00 00 00 00          mov    $0x0,%esi
  4020be:       bf 00 00 00 00          mov    $0x0,%edi
  4020c3:       e8 5d fc ff ff          callq  401d25 <notify_server>
  4020c8:       bf 01 00 00 00          mov    $0x1,%edi
  4020cd:       e8 5e ed ff ff          callq  400e30 <exit@plt>

00000000004020d2 <illegalhandler>:
  4020d2:       48 83 ec 08             sub    $0x8,%rsp
  4020d6:       83 3d 2b 34 20 00 00    cmpl   $0x0,0x20342b(%rip)        # 605508 <is_checker>
  4020dd:       74 16                   je     4020f5 <illegalhandler+0x23>
  4020df:       48 8d 3d 92 14 00 00    lea    0x1492(%rip),%rdi        # 403578 <_IO_stdin_used+0x4e8>
  4020e6:       e8 d5 eb ff ff          callq  400cc0 <puts@plt>
  4020eb:       b8 00 00 00 00          mov    $0x0,%eax
  4020f0:       e8 a6 fb ff ff          callq  401c9b <check_fail>
  4020f5:       48 8d 3d fc 15 00 00    lea    0x15fc(%rip),%rdi        # 4036f8 <_IO_stdin_used+0x668>
  4020fc:       e8 bf eb ff ff          callq  400cc0 <puts@plt>
  402101:       48 8d 3d 47 14 00 00    lea    0x1447(%rip),%rdi        # 40354f <_IO_stdin_used+0x4bf>
  402108:       e8 b3 eb ff ff          callq  400cc0 <puts@plt>
  40210d:       be 00 00 00 00          mov    $0x0,%esi
  402112:       bf 00 00 00 00          mov    $0x0,%edi
  402117:       e8 09 fc ff ff          callq  401d25 <notify_server>
  40211c:       bf 01 00 00 00          mov    $0x1,%edi
  402121:       e8 0a ed ff ff          callq  400e30 <exit@plt>

0000000000402126 <sigalrmhandler>:
  402126:       48 83 ec 08             sub    $0x8,%rsp
  40212a:       83 3d d7 33 20 00 00    cmpl   $0x0,0x2033d7(%rip)        # 605508 <is_checker>
  402131:       74 16                   je     402149 <sigalrmhandler+0x23>
  402133:       48 8d 3d 52 14 00 00    lea    0x1452(%rip),%rdi        # 40358c <_IO_stdin_used+0x4fc>
  40213a:       e8 81 eb ff ff          callq  400cc0 <puts@plt>
  40213f:       b8 00 00 00 00          mov    $0x0,%eax
  402144:       e8 52 fb ff ff          callq  401c9b <check_fail>
  402149:       ba 05 00 00 00          mov    $0x5,%edx
  40214e:       48 8d 35 d3 15 00 00    lea    0x15d3(%rip),%rsi        # 403728 <_IO_stdin_used+0x698>
  402155:       bf 01 00 00 00          mov    $0x1,%edi
  40215a:       b8 00 00 00 00          mov    $0x0,%eax
  40215f:       e8 7c ec ff ff          callq  400de0 <__printf_chk@plt>
  402164:       be 00 00 00 00          mov    $0x0,%esi
  402169:       bf 00 00 00 00          mov    $0x0,%edi
  40216e:       e8 b2 fb ff ff          callq  401d25 <notify_server>
  402173:       bf 01 00 00 00          mov    $0x1,%edi
  402178:       e8 b3 ec ff ff          callq  400e30 <exit@plt>

000000000040217d <launch>:
  40217d:       55                      push   %rbp
  40217e:       48 89 e5                mov    %rsp,%rbp
  402181:       48 83 ec 10             sub    $0x10,%rsp
  402185:       48 89 fa                mov    %rdi,%rdx
  402188:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  40218f:       00 00
  402191:       48 89 45 f8             mov    %rax,-0x8(%rbp)
  402195:       31 c0                   xor    %eax,%eax
  402197:       48 8d 47 1e             lea    0x1e(%rdi),%rax
  40219b:       48 83 e0 f0             and    $0xfffffffffffffff0,%rax
  40219f:       48 29 c4                sub    %rax,%rsp
  4021a2:       48 8d 7c 24 0f          lea    0xf(%rsp),%rdi
  4021a7:       48 83 e7 f0             and    $0xfffffffffffffff0,%rdi
  4021ab:       be f4 00 00 00          mov    $0xf4,%esi
  4021b0:       e8 4b eb ff ff          callq  400d00 <memset@plt>
  4021b5:       48 8b 05 e4 32 20 00    mov    0x2032e4(%rip),%rax        # 6054a0 <stdin@@GLIBC_2.2.5>
  4021bc:       48 39 05 2d 33 20 00    cmp    %rax,0x20332d(%rip)        # 6054f0 <infile>
  4021c3:       75 16                   jne    4021db <launch+0x5e>
  4021c5:       48 8d 35 c8 13 00 00    lea    0x13c8(%rip),%rsi        # 403594 <_IO_stdin_used+0x504>
  4021cc:       bf 01 00 00 00          mov    $0x1,%edi
  4021d1:       b8 00 00 00 00          mov    $0x0,%eax
  4021d6:       e8 05 ec ff ff          callq  400de0 <__printf_chk@plt>
  4021db:       c7 05 17 33 20 00 00    movl   $0x0,0x203317(%rip)        # 6054fc <vlevel>
  4021e2:       00 00 00
  4021e5:       b8 00 00 00 00          mov    $0x0,%eax
  4021ea:       e8 f8 f8 ff ff          callq  401ae7 <test>
  4021ef:       83 3d 12 33 20 00 00    cmpl   $0x0,0x203312(%rip)        # 605508 <is_checker>
  4021f6:       74 16                   je     40220e <launch+0x91>
  4021f8:       48 8d 3d a2 13 00 00    lea    0x13a2(%rip),%rdi        # 4035a1 <_IO_stdin_used+0x511>
  4021ff:       e8 bc ea ff ff          callq  400cc0 <puts@plt>
  402204:       b8 00 00 00 00          mov    $0x0,%eax
  402209:       e8 8d fa ff ff          callq  401c9b <check_fail>
  40220e:       48 8d 3d 97 13 00 00    lea    0x1397(%rip),%rdi        # 4035ac <_IO_stdin_used+0x51c>
  402215:       e8 a6 ea ff ff          callq  400cc0 <puts@plt>
  40221a:       48 8b 45 f8             mov    -0x8(%rbp),%rax
  40221e:       64 48 33 04 25 28 00    xor    %fs:0x28,%rax
  402225:       00 00
  402227:       74 05                   je     40222e <launch+0xb1>
  402229:       e8 b2 ea ff ff          callq  400ce0 <__stack_chk_fail@plt>
  40222e:       c9                      leaveq
  40222f:       c3                      retq

0000000000402230 <stable_launch>:
  402230:       53                      push   %rbx
  402231:       48 89 3d b0 32 20 00    mov    %rdi,0x2032b0(%rip)        # 6054e8 <global_offset>
  402238:       41 b9 00 00 00 00       mov    $0x0,%r9d
  40223e:       41 b8 00 00 00 00       mov    $0x0,%r8d
  402244:       b9 32 01 00 00          mov    $0x132,%ecx
  402249:       ba 07 00 00 00          mov    $0x7,%edx
  40224e:       be 00 00 10 00          mov    $0x100000,%esi
  402253:       bf 00 60 58 55          mov    $0x55586000,%edi
  402258:       e8 93 ea ff ff          callq  400cf0 <mmap@plt>
  40225d:       48 89 c3                mov    %rax,%rbx
  402260:       48 3d 00 60 58 55       cmp    $0x55586000,%rax
  402266:       74 39                   je     4022a1 <stable_launch+0x71>
  402268:       be 00 00 10 00          mov    $0x100000,%esi
  40226d:       48 89 c7                mov    %rax,%rdi
  402270:       e8 5b eb ff ff          callq  400dd0 <munmap@plt>
  402275:       b9 00 60 58 55          mov    $0x55586000,%ecx
  40227a:       48 8d 15 df 14 00 00    lea    0x14df(%rip),%rdx        # 403760 <_IO_stdin_used+0x6d0>
  402281:       be 01 00 00 00          mov    $0x1,%esi
  402286:       48 8b 3d 33 32 20 00    mov    0x203233(%rip),%rdi        # 6054c0 <stderr@@GLIBC_2.2.5>
  40228d:       b8 00 00 00 00          mov    $0x0,%eax
  402292:       e8 b9 eb ff ff          callq  400e50 <__fprintf_chk@plt>
  402297:       bf 01 00 00 00          mov    $0x1,%edi
  40229c:       e8 8f eb ff ff          callq  400e30 <exit@plt>
  4022a1:       48 8d 90 f8 ff 0f 00    lea    0xffff8(%rax),%rdx
  4022a8:       48 89 15 81 3e 20 00    mov    %rdx,0x203e81(%rip)        # 606130 <stack_top>
  4022af:       48 89 e0                mov    %rsp,%rax
  4022b2:       48 89 d4                mov    %rdx,%rsp
  4022b5:       48 89 c2                mov    %rax,%rdx
  4022b8:       48 89 15 21 32 20 00    mov    %rdx,0x203221(%rip)        # 6054e0 <global_save_stack>
  4022bf:       48 8b 3d 22 32 20 00    mov    0x203222(%rip),%rdi        # 6054e8 <global_offset>
  4022c6:       e8 b2 fe ff ff          callq  40217d <launch>
  4022cb:       48 8b 05 0e 32 20 00    mov    0x20320e(%rip),%rax        # 6054e0 <global_save_stack>
  4022d2:       48 89 c4                mov    %rax,%rsp
  4022d5:       be 00 00 10 00          mov    $0x100000,%esi
  4022da:       48 89 df                mov    %rbx,%rdi
  4022dd:       e8 ee ea ff ff          callq  400dd0 <munmap@plt>
  4022e2:       5b                      pop    %rbx
  4022e3:       c3                      retq

00000000004022e4 <rio_readinitb>:
  4022e4:       89 37                   mov    %esi,(%rdi)
  4022e6:       c7 47 04 00 00 00 00    movl   $0x0,0x4(%rdi)
  4022ed:       48 8d 47 10             lea    0x10(%rdi),%rax
  4022f1:       48 89 47 08             mov    %rax,0x8(%rdi)
  4022f5:       c3                      retq

00000000004022f6 <sigalrm_handler>:
  4022f6:       48 83 ec 08             sub    $0x8,%rsp
  4022fa:       b9 00 00 00 00          mov    $0x0,%ecx
  4022ff:       48 8d 15 9a 14 00 00    lea    0x149a(%rip),%rdx        # 4037a0 <trans_char+0x10>
  402306:       be 01 00 00 00          mov    $0x1,%esi
  40230b:       48 8b 3d ae 31 20 00    mov    0x2031ae(%rip),%rdi        # 6054c0 <stderr@@GLIBC_2.2.5>
  402312:       b8 00 00 00 00          mov    $0x0,%eax
  402317:       e8 34 eb ff ff          callq  400e50 <__fprintf_chk@plt>
  40231c:       bf 01 00 00 00          mov    $0x1,%edi
  402321:       e8 0a eb ff ff          callq  400e30 <exit@plt>

0000000000402326 <rio_writen>:
  402326:       41 55                   push   %r13
  402328:       41 54                   push   %r12
  40232a:       55                      push   %rbp
  40232b:       53                      push   %rbx
  40232c:       48 83 ec 08             sub    $0x8,%rsp
  402330:       41 89 fc                mov    %edi,%r12d
  402333:       48 89 f5                mov    %rsi,%rbp
  402336:       49 89 d5                mov    %rdx,%r13
  402339:       48 89 d3                mov    %rdx,%rbx
  40233c:       eb 28                   jmp    402366 <rio_writen+0x40>
  40233e:       48 89 da                mov    %rbx,%rdx
  402341:       48 89 ee                mov    %rbp,%rsi
  402344:       44 89 e7                mov    %r12d,%edi
  402347:       e8 84 e9 ff ff          callq  400cd0 <write@plt>
  40234c:       48 85 c0                test   %rax,%rax
  40234f:       7f 0f                   jg     402360 <rio_writen+0x3a>
  402351:       e8 2a e9 ff ff          callq  400c80 <__errno_location@plt>
  402356:       83 38 04                cmpl   $0x4,(%rax)
  402359:       75 15                   jne    402370 <rio_writen+0x4a>
  40235b:       b8 00 00 00 00          mov    $0x0,%eax
  402360:       48 29 c3                sub    %rax,%rbx
  402363:       48 01 c5                add    %rax,%rbp
  402366:       48 85 db                test   %rbx,%rbx
  402369:       75 d3                   jne    40233e <rio_writen+0x18>
  40236b:       4c 89 e8                mov    %r13,%rax
  40236e:       eb 07                   jmp    402377 <rio_writen+0x51>
  402370:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  402377:       48 83 c4 08             add    $0x8,%rsp
  40237b:       5b                      pop    %rbx
  40237c:       5d                      pop    %rbp
  40237d:       41 5c                   pop    %r12
  40237f:       41 5d                   pop    %r13
  402381:       c3                      retq

0000000000402382 <rio_read>:
  402382:       41 55                   push   %r13
  402384:       41 54                   push   %r12
  402386:       55                      push   %rbp
  402387:       53                      push   %rbx
  402388:       48 83 ec 08             sub    $0x8,%rsp
  40238c:       48 89 fb                mov    %rdi,%rbx
  40238f:       49 89 f5                mov    %rsi,%r13
  402392:       49 89 d4                mov    %rdx,%r12
  402395:       eb 2e                   jmp    4023c5 <rio_read+0x43>
  402397:       48 8d 6b 10             lea    0x10(%rbx),%rbp
  40239b:       8b 3b                   mov    (%rbx),%edi
  40239d:       ba 00 20 00 00          mov    $0x2000,%edx
  4023a2:       48 89 ee                mov    %rbp,%rsi
  4023a5:       e8 86 e9 ff ff          callq  400d30 <read@plt>
  4023aa:       89 43 04                mov    %eax,0x4(%rbx)
  4023ad:       85 c0                   test   %eax,%eax
  4023af:       79 0c                   jns    4023bd <rio_read+0x3b>
  4023b1:       e8 ca e8 ff ff          callq  400c80 <__errno_location@plt>
  4023b6:       83 38 04                cmpl   $0x4,(%rax)
  4023b9:       74 0a                   je     4023c5 <rio_read+0x43>
  4023bb:       eb 37                   jmp    4023f4 <rio_read+0x72>
  4023bd:       85 c0                   test   %eax,%eax
  4023bf:       74 3c                   je     4023fd <rio_read+0x7b>
  4023c1:       48 89 6b 08             mov    %rbp,0x8(%rbx)
  4023c5:       8b 6b 04                mov    0x4(%rbx),%ebp
  4023c8:       85 ed                   test   %ebp,%ebp
  4023ca:       7e cb                   jle    402397 <rio_read+0x15>
  4023cc:       89 e8                   mov    %ebp,%eax
  4023ce:       49 39 c4                cmp    %rax,%r12
  4023d1:       77 03                   ja     4023d6 <rio_read+0x54>
  4023d3:       44 89 e5                mov    %r12d,%ebp
  4023d6:       4c 63 e5                movslq %ebp,%r12
  4023d9:       48 8b 73 08             mov    0x8(%rbx),%rsi
  4023dd:       4c 89 e2                mov    %r12,%rdx
  4023e0:       4c 89 ef                mov    %r13,%rdi
  4023e3:       e8 98 e9 ff ff          callq  400d80 <memcpy@plt>
  4023e8:       4c 01 63 08             add    %r12,0x8(%rbx)
  4023ec:       29 6b 04                sub    %ebp,0x4(%rbx)
  4023ef:       4c 89 e0                mov    %r12,%rax
  4023f2:       eb 0e                   jmp    402402 <rio_read+0x80>
  4023f4:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  4023fb:       eb 05                   jmp    402402 <rio_read+0x80>
  4023fd:       b8 00 00 00 00          mov    $0x0,%eax
  402402:       48 83 c4 08             add    $0x8,%rsp
  402406:       5b                      pop    %rbx
  402407:       5d                      pop    %rbp
  402408:       41 5c                   pop    %r12
  40240a:       41 5d                   pop    %r13
  40240c:       c3                      retq

000000000040240d <rio_readlineb>:
  40240d:       41 55                   push   %r13
  40240f:       41 54                   push   %r12
  402411:       55                      push   %rbp
  402412:       53                      push   %rbx
  402413:       48 83 ec 18             sub    $0x18,%rsp
  402417:       49 89 fd                mov    %rdi,%r13
  40241a:       48 89 f5                mov    %rsi,%rbp
  40241d:       49 89 d4                mov    %rdx,%r12
  402420:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  402427:       00 00
  402429:       48 89 44 24 08          mov    %rax,0x8(%rsp)
  40242e:       31 c0                   xor    %eax,%eax
  402430:       bb 01 00 00 00          mov    $0x1,%ebx
  402435:       eb 3f                   jmp    402476 <rio_readlineb+0x69>
  402437:       48 8d 74 24 07          lea    0x7(%rsp),%rsi
  40243c:       ba 01 00 00 00          mov    $0x1,%edx
  402441:       4c 89 ef                mov    %r13,%rdi
  402444:       e8 39 ff ff ff          callq  402382 <rio_read>
  402449:       83 f8 01                cmp    $0x1,%eax
  40244c:       75 15                   jne    402463 <rio_readlineb+0x56>
  40244e:       48 8d 45 01             lea    0x1(%rbp),%rax
  402452:       0f b6 54 24 07          movzbl 0x7(%rsp),%edx
  402457:       88 55 00                mov    %dl,0x0(%rbp)
  40245a:       80 7c 24 07 0a          cmpb   $0xa,0x7(%rsp)
  40245f:       75 0e                   jne    40246f <rio_readlineb+0x62>
  402461:       eb 1a                   jmp    40247d <rio_readlineb+0x70>
  402463:       85 c0                   test   %eax,%eax
  402465:       75 22                   jne    402489 <rio_readlineb+0x7c>
  402467:       48 83 fb 01             cmp    $0x1,%rbx
  40246b:       75 13                   jne    402480 <rio_readlineb+0x73>
  40246d:       eb 23                   jmp    402492 <rio_readlineb+0x85>
  40246f:       48 83 c3 01             add    $0x1,%rbx
  402473:       48 89 c5                mov    %rax,%rbp
  402476:       4c 39 e3                cmp    %r12,%rbx
  402479:       72 bc                   jb     402437 <rio_readlineb+0x2a>
  40247b:       eb 03                   jmp    402480 <rio_readlineb+0x73>
  40247d:       48 89 c5                mov    %rax,%rbp
  402480:       c6 45 00 00             movb   $0x0,0x0(%rbp)
  402484:       48 89 d8                mov    %rbx,%rax
  402487:       eb 0e                   jmp    402497 <rio_readlineb+0x8a>
  402489:       48 c7 c0 ff ff ff ff    mov    $0xffffffffffffffff,%rax
  402490:       eb 05                   jmp    402497 <rio_readlineb+0x8a>
  402492:       b8 00 00 00 00          mov    $0x0,%eax
  402497:       48 8b 4c 24 08          mov    0x8(%rsp),%rcx
  40249c:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
  4024a3:       00 00
  4024a5:       74 05                   je     4024ac <rio_readlineb+0x9f>
  4024a7:       e8 34 e8 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  4024ac:       48 83 c4 18             add    $0x18,%rsp
  4024b0:       5b                      pop    %rbx
  4024b1:       5d                      pop    %rbp
  4024b2:       41 5c                   pop    %r12
  4024b4:       41 5d                   pop    %r13
  4024b6:       c3                      retq

00000000004024b7 <urlencode>:
  4024b7:       41 54                   push   %r12
  4024b9:       55                      push   %rbp
  4024ba:       53                      push   %rbx
  4024bb:       48 83 ec 10             sub    $0x10,%rsp
  4024bf:       48 89 fb                mov    %rdi,%rbx
  4024c2:       48 89 f5                mov    %rsi,%rbp
  4024c5:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4024cc:       00 00
  4024ce:       48 89 44 24 08          mov    %rax,0x8(%rsp)
  4024d3:       31 c0                   xor    %eax,%eax
  4024d5:       48 c7 c1 ff ff ff ff    mov    $0xffffffffffffffff,%rcx
  4024dc:       f2 ae                   repnz scas %es:(%rdi),%al
  4024de:       48 f7 d1                not    %rcx
  4024e1:       8d 41 ff                lea    -0x1(%rcx),%eax
  4024e4:       e9 ac 00 00 00          jmpq   402595 <urlencode+0xde>
  4024e9:       44 0f b6 03             movzbl (%rbx),%r8d
  4024ed:       41 80 f8 2a             cmp    $0x2a,%r8b
  4024f1:       0f 94 c2                sete   %dl
  4024f4:       41 80 f8 2d             cmp    $0x2d,%r8b
  4024f8:       0f 94 c0                sete   %al
  4024fb:       08 c2                   or     %al,%dl
  4024fd:       75 24                   jne    402523 <urlencode+0x6c>
  4024ff:       41 80 f8 2e             cmp    $0x2e,%r8b
  402503:       74 1e                   je     402523 <urlencode+0x6c>
  402505:       41 80 f8 5f             cmp    $0x5f,%r8b
  402509:       74 18                   je     402523 <urlencode+0x6c>
  40250b:       41 8d 40 d0             lea    -0x30(%r8),%eax
  40250f:       3c 09                   cmp    $0x9,%al
  402511:       76 10                   jbe    402523 <urlencode+0x6c>
  402513:       41 8d 40 bf             lea    -0x41(%r8),%eax
  402517:       3c 19                   cmp    $0x19,%al
  402519:       76 08                   jbe    402523 <urlencode+0x6c>
  40251b:       41 8d 40 9f             lea    -0x61(%r8),%eax
  40251f:       3c 19                   cmp    $0x19,%al
  402521:       77 0a                   ja     40252d <urlencode+0x76>
  402523:       44 88 45 00             mov    %r8b,0x0(%rbp)
  402527:       48 8d 6d 01             lea    0x1(%rbp),%rbp
  40252b:       eb 61                   jmp    40258e <urlencode+0xd7>
  40252d:       41 80 f8 20             cmp    $0x20,%r8b
  402531:       75 0a                   jne    40253d <urlencode+0x86>
  402533:       c6 45 00 2b             movb   $0x2b,0x0(%rbp)
  402537:       48 8d 6d 01             lea    0x1(%rbp),%rbp
  40253b:       eb 51                   jmp    40258e <urlencode+0xd7>
  40253d:       41 8d 40 e0             lea    -0x20(%r8),%eax
  402541:       3c 5f                   cmp    $0x5f,%al
  402543:       0f 96 c2                setbe  %dl
  402546:       41 80 f8 09             cmp    $0x9,%r8b
  40254a:       0f 94 c0                sete   %al
  40254d:       08 c2                   or     %al,%dl
  40254f:       74 52                   je     4025a3 <urlencode+0xec>
  402551:       48 89 e7                mov    %rsp,%rdi
  402554:       45 0f b6 c0             movzbl %r8b,%r8d
  402558:       48 8d 0d d9 12 00 00    lea    0x12d9(%rip),%rcx        # 403838 <trans_char+0xa8>
  40255f:       ba 08 00 00 00          mov    $0x8,%edx
  402564:       be 01 00 00 00          mov    $0x1,%esi
  402569:       b8 00 00 00 00          mov    $0x0,%eax
  40256e:       e8 ed e8 ff ff          callq  400e60 <__sprintf_chk@plt>
  402573:       0f b6 04 24             movzbl (%rsp),%eax
  402577:       88 45 00                mov    %al,0x0(%rbp)
  40257a:       0f b6 44 24 01          movzbl 0x1(%rsp),%eax
  40257f:       88 45 01                mov    %al,0x1(%rbp)
  402582:       0f b6 44 24 02          movzbl 0x2(%rsp),%eax
  402587:       88 45 02                mov    %al,0x2(%rbp)
  40258a:       48 8d 6d 03             lea    0x3(%rbp),%rbp
  40258e:       48 83 c3 01             add    $0x1,%rbx
  402592:       44 89 e0                mov    %r12d,%eax
  402595:       44 8d 60 ff             lea    -0x1(%rax),%r12d
  402599:       85 c0                   test   %eax,%eax
  40259b:       0f 85 48 ff ff ff       jne    4024e9 <urlencode+0x32>
  4025a1:       eb 05                   jmp    4025a8 <urlencode+0xf1>
  4025a3:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  4025a8:       48 8b 74 24 08          mov    0x8(%rsp),%rsi
  4025ad:       64 48 33 34 25 28 00    xor    %fs:0x28,%rsi
  4025b4:       00 00
  4025b6:       74 05                   je     4025bd <urlencode+0x106>
  4025b8:       e8 23 e7 ff ff          callq  400ce0 <__stack_chk_fail@plt>
  4025bd:       48 83 c4 10             add    $0x10,%rsp
  4025c1:       5b                      pop    %rbx
  4025c2:       5d                      pop    %rbp
  4025c3:       41 5c                   pop    %r12
  4025c5:       c3                      retq

00000000004025c6 <submitr>:
  4025c6:       41 57                   push   %r15
  4025c8:       41 56                   push   %r14
  4025ca:       41 55                   push   %r13
  4025cc:       41 54                   push   %r12
  4025ce:       55                      push   %rbp
  4025cf:       53                      push   %rbx
  4025d0:       48 81 ec 68 a0 00 00    sub    $0xa068,%rsp
  4025d7:       49 89 fd                mov    %rdi,%r13
  4025da:       89 74 24 14             mov    %esi,0x14(%rsp)
  4025de:       49 89 d7                mov    %rdx,%r15
  4025e1:       48 89 4c 24 08          mov    %rcx,0x8(%rsp)
  4025e6:       4c 89 44 24 18          mov    %r8,0x18(%rsp)
  4025eb:       4d 89 ce                mov    %r9,%r14
  4025ee:       48 8b 9c 24 a0 a0 00    mov    0xa0a0(%rsp),%rbx
  4025f5:       00
  4025f6:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  4025fd:       00 00
  4025ff:       48 89 84 24 58 a0 00    mov    %rax,0xa058(%rsp)
  402606:       00
  402607:       31 c0                   xor    %eax,%eax
  402609:       c7 44 24 2c 00 00 00    movl   $0x0,0x2c(%rsp)
  402610:       00
  402611:       ba 00 00 00 00          mov    $0x0,%edx
  402616:       be 01 00 00 00          mov    $0x1,%esi
  40261b:       bf 02 00 00 00          mov    $0x2,%edi
  402620:       e8 4b e8 ff ff          callq  400e70 <socket@plt>
  402625:       85 c0                   test   %eax,%eax
  402627:       79 4e                   jns    402677 <submitr+0xb1>
  402629:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402630:       3a 20 43
  402633:       48 89 03                mov    %rax,(%rbx)
  402636:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  40263d:       20 75 6e
  402640:       48 89 43 08             mov    %rax,0x8(%rbx)
  402644:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  40264b:       74 6f 20
  40264e:       48 89 43 10             mov    %rax,0x10(%rbx)
  402652:       48 b8 63 72 65 61 74    movabs $0x7320657461657263,%rax
  402659:       65 20 73
  40265c:       48 89 43 18             mov    %rax,0x18(%rbx)
  402660:       c7 43 20 6f 63 6b 65    movl   $0x656b636f,0x20(%rbx)
  402667:       66 c7 43 24 74 00       movw   $0x74,0x24(%rbx)
  40266d:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402672:       e9 77 06 00 00          jmpq   402cee <submitr+0x728>
  402677:       89 c5                   mov    %eax,%ebp
  402679:       4c 89 ef                mov    %r13,%rdi
  40267c:       e8 cf e6 ff ff          callq  400d50 <gethostbyname@plt>
  402681:       48 85 c0                test   %rax,%rax
  402684:       75 67                   jne    4026ed <submitr+0x127>
  402686:       48 b8 45 72 72 6f 72    movabs $0x44203a726f727245,%rax
  40268d:       3a 20 44
  402690:       48 89 03                mov    %rax,(%rbx)
  402693:       48 b8 4e 53 20 69 73    movabs $0x6e7520736920534e,%rax
  40269a:       20 75 6e
  40269d:       48 89 43 08             mov    %rax,0x8(%rbx)
  4026a1:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  4026a8:       74 6f 20
  4026ab:       48 89 43 10             mov    %rax,0x10(%rbx)
  4026af:       48 b8 72 65 73 6f 6c    movabs $0x2065766c6f736572,%rax
  4026b6:       76 65 20
  4026b9:       48 89 43 18             mov    %rax,0x18(%rbx)
  4026bd:       48 b8 73 65 72 76 65    movabs $0x6120726576726573,%rax
  4026c4:       72 20 61
  4026c7:       48 89 43 20             mov    %rax,0x20(%rbx)
  4026cb:       c7 43 28 64 64 72 65    movl   $0x65726464,0x28(%rbx)
  4026d2:       66 c7 43 2c 73 73       movw   $0x7373,0x2c(%rbx)
  4026d8:       c6 43 2e 00             movb   $0x0,0x2e(%rbx)
  4026dc:       89 ef                   mov    %ebp,%edi
  4026de:       e8 3d e6 ff ff          callq  400d20 <close@plt>
  4026e3:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  4026e8:       e9 01 06 00 00          jmpq   402cee <submitr+0x728>
  4026ed:       4c 8d 64 24 30          lea    0x30(%rsp),%r12
  4026f2:       48 c7 44 24 30 00 00    movq   $0x0,0x30(%rsp)
  4026f9:       00 00
  4026fb:       48 c7 44 24 38 00 00    movq   $0x0,0x38(%rsp)
  402702:       00 00
  402704:       66 c7 44 24 30 02 00    movw   $0x2,0x30(%rsp)
  40270b:       48 63 50 14             movslq 0x14(%rax),%rdx
  40270f:       48 8b 40 18             mov    0x18(%rax),%rax
  402713:       48 8b 30                mov    (%rax),%rsi
  402716:       48 8d 7c 24 34          lea    0x34(%rsp),%rdi
  40271b:       b9 0c 00 00 00          mov    $0xc,%ecx
  402720:       e8 3b e6 ff ff          callq  400d60 <__memmove_chk@plt>
  402725:       0f b7 44 24 14          movzwl 0x14(%rsp),%eax
  40272a:       66 c1 c8 08             ror    $0x8,%ax
  40272e:       66 89 44 24 32          mov    %ax,0x32(%rsp)
  402733:       ba 10 00 00 00          mov    $0x10,%edx
  402738:       4c 89 e6                mov    %r12,%rsi
  40273b:       89 ef                   mov    %ebp,%edi
  40273d:       e8 fe e6 ff ff          callq  400e40 <connect@plt>
  402742:       85 c0                   test   %eax,%eax
  402744:       79 59                   jns    40279f <submitr+0x1d9>
  402746:       48 b8 45 72 72 6f 72    movabs $0x55203a726f727245,%rax
  40274d:       3a 20 55
  402750:       48 89 03                mov    %rax,(%rbx)
  402753:       48 b8 6e 61 62 6c 65    movabs $0x6f7420656c62616e,%rax
  40275a:       20 74 6f
  40275d:       48 89 43 08             mov    %rax,0x8(%rbx)
  402761:       48 b8 20 63 6f 6e 6e    movabs $0x7463656e6e6f6320,%rax
  402768:       65 63 74
  40276b:       48 89 43 10             mov    %rax,0x10(%rbx)
  40276f:       48 b8 20 74 6f 20 74    movabs $0x20656874206f7420,%rax
  402776:       68 65 20
  402779:       48 89 43 18             mov    %rax,0x18(%rbx)
  40277d:       c7 43 20 73 65 72 76    movl   $0x76726573,0x20(%rbx)
  402784:       66 c7 43 24 65 72       movw   $0x7265,0x24(%rbx)
  40278a:       c6 43 26 00             movb   $0x0,0x26(%rbx)
  40278e:       89 ef                   mov    %ebp,%edi
  402790:       e8 8b e5 ff ff          callq  400d20 <close@plt>
  402795:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  40279a:       e9 4f 05 00 00          jmpq   402cee <submitr+0x728>
  40279f:       48 c7 c6 ff ff ff ff    mov    $0xffffffffffffffff,%rsi
  4027a6:       b8 00 00 00 00          mov    $0x0,%eax
  4027ab:       48 89 f1                mov    %rsi,%rcx
  4027ae:       4c 89 f7                mov    %r14,%rdi
  4027b1:       f2 ae                   repnz scas %es:(%rdi),%al
  4027b3:       48 89 ca                mov    %rcx,%rdx
  4027b6:       48 f7 d2                not    %rdx
  4027b9:       48 89 f1                mov    %rsi,%rcx
  4027bc:       4c 89 ff                mov    %r15,%rdi
  4027bf:       f2 ae                   repnz scas %es:(%rdi),%al
  4027c1:       48 f7 d1                not    %rcx
  4027c4:       49 89 c8                mov    %rcx,%r8
  4027c7:       48 89 f1                mov    %rsi,%rcx
  4027ca:       48 8b 7c 24 08          mov    0x8(%rsp),%rdi
  4027cf:       f2 ae                   repnz scas %es:(%rdi),%al
  4027d1:       48 f7 d1                not    %rcx
  4027d4:       4d 8d 44 08 fe          lea    -0x2(%r8,%rcx,1),%r8
  4027d9:       48 89 f1                mov    %rsi,%rcx
  4027dc:       48 8b 7c 24 18          mov    0x18(%rsp),%rdi
  4027e1:       f2 ae                   repnz scas %es:(%rdi),%al
  4027e3:       48 89 c8                mov    %rcx,%rax
  4027e6:       48 f7 d0                not    %rax
  4027e9:       49 8d 4c 00 ff          lea    -0x1(%r8,%rax,1),%rcx
  4027ee:       48 8d 44 52 fd          lea    -0x3(%rdx,%rdx,2),%rax
  4027f3:       48 8d 84 01 80 00 00    lea    0x80(%rcx,%rax,1),%rax
  4027fa:       00
  4027fb:       48 3d 00 20 00 00       cmp    $0x2000,%rax
  402801:       76 72                   jbe    402875 <submitr+0x2af>
  402803:       48 b8 45 72 72 6f 72    movabs $0x52203a726f727245,%rax
  40280a:       3a 20 52
  40280d:       48 89 03                mov    %rax,(%rbx)
  402810:       48 b8 65 73 75 6c 74    movabs $0x747320746c757365,%rax
  402817:       20 73 74
  40281a:       48 89 43 08             mov    %rax,0x8(%rbx)
  40281e:       48 b8 72 69 6e 67 20    movabs $0x6f6f7420676e6972,%rax
  402825:       74 6f 6f
  402828:       48 89 43 10             mov    %rax,0x10(%rbx)
  40282c:       48 b8 20 6c 61 72 67    movabs $0x202e656772616c20,%rax
  402833:       65 2e 20
  402836:       48 89 43 18             mov    %rax,0x18(%rbx)
  40283a:       48 b8 49 6e 63 72 65    movabs $0x6573616572636e49,%rax
  402841:       61 73 65
  402844:       48 89 43 20             mov    %rax,0x20(%rbx)
  402848:       48 b8 20 53 55 42 4d    movabs $0x5254494d42555320,%rax
  40284f:       49 54 52
  402852:       48 89 43 28             mov    %rax,0x28(%rbx)
  402856:       48 b8 5f 4d 41 58 42    movabs $0x46554258414d5f,%rax
  40285d:       55 46 00
  402860:       48 89 43 30             mov    %rax,0x30(%rbx)
  402864:       89 ef                   mov    %ebp,%edi
  402866:       e8 b5 e4 ff ff          callq  400d20 <close@plt>
  40286b:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402870:       e9 79 04 00 00          jmpq   402cee <submitr+0x728>
  402875:       48 8d b4 24 50 40 00    lea    0x4050(%rsp),%rsi
  40287c:       00
  40287d:       b9 00 04 00 00          mov    $0x400,%ecx
  402882:       b8 00 00 00 00          mov    $0x0,%eax
  402887:       48 89 f7                mov    %rsi,%rdi
  40288a:       f3 48 ab                rep stos %rax,%es:(%rdi)
  40288d:       4c 89 f7                mov    %r14,%rdi
  402890:       e8 22 fc ff ff          callq  4024b7 <urlencode>
  402895:       85 c0                   test   %eax,%eax
  402897:       0f 89 8a 00 00 00       jns    402927 <submitr+0x361>
  40289d:       48 b8 45 72 72 6f 72    movabs $0x52203a726f727245,%rax
  4028a4:       3a 20 52
  4028a7:       48 89 03                mov    %rax,(%rbx)
  4028aa:       48 b8 65 73 75 6c 74    movabs $0x747320746c757365,%rax
  4028b1:       20 73 74
  4028b4:       48 89 43 08             mov    %rax,0x8(%rbx)
  4028b8:       48 b8 72 69 6e 67 20    movabs $0x6e6f6320676e6972,%rax
  4028bf:       63 6f 6e
  4028c2:       48 89 43 10             mov    %rax,0x10(%rbx)
  4028c6:       48 b8 74 61 69 6e 73    movabs $0x6e6120736e696174,%rax
  4028cd:       20 61 6e
  4028d0:       48 89 43 18             mov    %rax,0x18(%rbx)
  4028d4:       48 b8 20 69 6c 6c 65    movabs $0x6c6167656c6c6920,%rax
  4028db:       67 61 6c
  4028de:       48 89 43 20             mov    %rax,0x20(%rbx)
  4028e2:       48 b8 20 6f 72 20 75    movabs $0x72706e7520726f20,%rax
  4028e9:       6e 70 72
  4028ec:       48 89 43 28             mov    %rax,0x28(%rbx)
  4028f0:       48 b8 69 6e 74 61 62    movabs $0x20656c6261746e69,%rax
  4028f7:       6c 65 20
  4028fa:       48 89 43 30             mov    %rax,0x30(%rbx)
  4028fe:       48 b8 63 68 61 72 61    movabs $0x6574636172616863,%rax
  402905:       63 74 65
  402908:       48 89 43 38             mov    %rax,0x38(%rbx)
  40290c:       66 c7 43 40 72 2e       movw   $0x2e72,0x40(%rbx)
  402912:       c6 43 42 00             movb   $0x0,0x42(%rbx)
  402916:       89 ef                   mov    %ebp,%edi
  402918:       e8 03 e4 ff ff          callq  400d20 <close@plt>
  40291d:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402922:       e9 c7 03 00 00          jmpq   402cee <submitr+0x728>
  402927:       4c 8d a4 24 50 20 00    lea    0x2050(%rsp),%r12
  40292e:       00
  40292f:       41 55                   push   %r13
  402931:       48 8d 84 24 58 40 00    lea    0x4058(%rsp),%rax
  402938:       00
  402939:       50                      push   %rax
  40293a:       4d 89 f9                mov    %r15,%r9
  40293d:       4c 8b 44 24 18          mov    0x18(%rsp),%r8
  402942:       48 8d 0d 7f 0e 00 00    lea    0xe7f(%rip),%rcx        # 4037c8 <trans_char+0x38>
  402949:       ba 00 20 00 00          mov    $0x2000,%edx
  40294e:       be 01 00 00 00          mov    $0x1,%esi
  402953:       4c 89 e7                mov    %r12,%rdi
  402956:       b8 00 00 00 00          mov    $0x0,%eax
  40295b:       e8 00 e5 ff ff          callq  400e60 <__sprintf_chk@plt>
  402960:       b8 00 00 00 00          mov    $0x0,%eax
  402965:       48 c7 c1 ff ff ff ff    mov    $0xffffffffffffffff,%rcx
  40296c:       4c 89 e7                mov    %r12,%rdi
  40296f:       f2 ae                   repnz scas %es:(%rdi),%al
  402971:       48 f7 d1                not    %rcx
  402974:       48 8d 51 ff             lea    -0x1(%rcx),%rdx
  402978:       4c 89 e6                mov    %r12,%rsi
  40297b:       89 ef                   mov    %ebp,%edi
  40297d:       e8 a4 f9 ff ff          callq  402326 <rio_writen>
  402982:       48 83 c4 10             add    $0x10,%rsp
  402986:       48 85 c0                test   %rax,%rax
  402989:       79 6e                   jns    4029f9 <submitr+0x433>
  40298b:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402992:       3a 20 43
  402995:       48 89 03                mov    %rax,(%rbx)
  402998:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  40299f:       20 75 6e
  4029a2:       48 89 43 08             mov    %rax,0x8(%rbx)
  4029a6:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  4029ad:       74 6f 20
  4029b0:       48 89 43 10             mov    %rax,0x10(%rbx)
  4029b4:       48 b8 77 72 69 74 65    movabs $0x6f74206574697277,%rax
  4029bb:       20 74 6f
  4029be:       48 89 43 18             mov    %rax,0x18(%rbx)
  4029c2:       48 b8 20 74 68 65 20    movabs $0x7365722065687420,%rax
  4029c9:       72 65 73
  4029cc:       48 89 43 20             mov    %rax,0x20(%rbx)
  4029d0:       48 b8 75 6c 74 20 73    movabs $0x7672657320746c75,%rax
  4029d7:       65 72 76
  4029da:       48 89 43 28             mov    %rax,0x28(%rbx)
  4029de:       66 c7 43 30 65 72       movw   $0x7265,0x30(%rbx)
  4029e4:       c6 43 32 00             movb   $0x0,0x32(%rbx)
  4029e8:       89 ef                   mov    %ebp,%edi
  4029ea:       e8 31 e3 ff ff          callq  400d20 <close@plt>
  4029ef:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  4029f4:       e9 f5 02 00 00          jmpq   402cee <submitr+0x728>
  4029f9:       4c 8d 64 24 40          lea    0x40(%rsp),%r12
  4029fe:       89 ee                   mov    %ebp,%esi
  402a00:       4c 89 e7                mov    %r12,%rdi
  402a03:       e8 dc f8 ff ff          callq  4022e4 <rio_readinitb>
  402a08:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402a0f:       00
  402a10:       ba 00 20 00 00          mov    $0x2000,%edx
  402a15:       4c 89 e7                mov    %r12,%rdi
  402a18:       e8 f0 f9 ff ff          callq  40240d <rio_readlineb>
  402a1d:       48 85 c0                test   %rax,%rax
  402a20:       7f 7d                   jg     402a9f <submitr+0x4d9>
  402a22:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402a29:       3a 20 43
  402a2c:       48 89 03                mov    %rax,(%rbx)
  402a2f:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402a36:       20 75 6e
  402a39:       48 89 43 08             mov    %rax,0x8(%rbx)
  402a3d:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402a44:       74 6f 20
  402a47:       48 89 43 10             mov    %rax,0x10(%rbx)
  402a4b:       48 b8 72 65 61 64 20    movabs $0x7269662064616572,%rax
  402a52:       66 69 72
  402a55:       48 89 43 18             mov    %rax,0x18(%rbx)
  402a59:       48 b8 73 74 20 68 65    movabs $0x6564616568207473,%rax
  402a60:       61 64 65
  402a63:       48 89 43 20             mov    %rax,0x20(%rbx)
  402a67:       48 b8 72 20 66 72 6f    movabs $0x72206d6f72662072,%rax
  402a6e:       6d 20 72
  402a71:       48 89 43 28             mov    %rax,0x28(%rbx)
  402a75:       48 b8 65 73 75 6c 74    movabs $0x657320746c757365,%rax
  402a7c:       20 73 65
  402a7f:       48 89 43 30             mov    %rax,0x30(%rbx)
  402a83:       c7 43 38 72 76 65 72    movl   $0x72657672,0x38(%rbx)
  402a8a:       c6 43 3c 00             movb   $0x0,0x3c(%rbx)
  402a8e:       89 ef                   mov    %ebp,%edi
  402a90:       e8 8b e2 ff ff          callq  400d20 <close@plt>
  402a95:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402a9a:       e9 4f 02 00 00          jmpq   402cee <submitr+0x728>
  402a9f:       48 8d 4c 24 2c          lea    0x2c(%rsp),%rcx
  402aa4:       48 8d 94 24 50 60 00    lea    0x6050(%rsp),%rdx
  402aab:       00
  402aac:       48 8d bc 24 50 20 00    lea    0x2050(%rsp),%rdi
  402ab3:       00
  402ab4:       4c 8d 84 24 50 80 00    lea    0x8050(%rsp),%r8
  402abb:       00
  402abc:       48 8d 35 7c 0d 00 00    lea    0xd7c(%rip),%rsi        # 40383f <trans_char+0xaf>
  402ac3:       b8 00 00 00 00          mov    $0x0,%eax
  402ac8:       e8 f3 e2 ff ff          callq  400dc0 <__isoc99_sscanf@plt>
  402acd:       e9 95 00 00 00          jmpq   402b67 <submitr+0x5a1>
  402ad2:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402ad9:       00
  402ada:       48 8d 7c 24 40          lea    0x40(%rsp),%rdi
  402adf:       ba 00 20 00 00          mov    $0x2000,%edx
  402ae4:       e8 24 f9 ff ff          callq  40240d <rio_readlineb>
  402ae9:       48 85 c0                test   %rax,%rax
  402aec:       7f 79                   jg     402b67 <submitr+0x5a1>
  402aee:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402af5:       3a 20 43
  402af8:       48 89 03                mov    %rax,(%rbx)
  402afb:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402b02:       20 75 6e
  402b05:       48 89 43 08             mov    %rax,0x8(%rbx)
  402b09:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402b10:       74 6f 20
  402b13:       48 89 43 10             mov    %rax,0x10(%rbx)
  402b17:       48 b8 72 65 61 64 20    movabs $0x6165682064616572,%rax
  402b1e:       68 65 61
  402b21:       48 89 43 18             mov    %rax,0x18(%rbx)
  402b25:       48 b8 64 65 72 73 20    movabs $0x6f72662073726564,%rax
  402b2c:       66 72 6f
  402b2f:       48 89 43 20             mov    %rax,0x20(%rbx)
  402b33:       48 b8 6d 20 74 68 65    movabs $0x657220656874206d,%rax
  402b3a:       20 72 65
  402b3d:       48 89 43 28             mov    %rax,0x28(%rbx)
  402b41:       48 b8 73 75 6c 74 20    movabs $0x72657320746c7573,%rax
  402b48:       73 65 72
  402b4b:       48 89 43 30             mov    %rax,0x30(%rbx)
  402b4f:       c7 43 38 76 65 72 00    movl   $0x726576,0x38(%rbx)
  402b56:       89 ef                   mov    %ebp,%edi
  402b58:       e8 c3 e1 ff ff          callq  400d20 <close@plt>
  402b5d:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402b62:       e9 87 01 00 00          jmpq   402cee <submitr+0x728>
  402b67:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402b6e:       00
  402b6f:       b9 03 00 00 00          mov    $0x3,%ecx
  402b74:       48 8d 3d db 0c 00 00    lea    0xcdb(%rip),%rdi        # 403856 <trans_char+0xc6>
  402b7b:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402b7d:       0f 97 c2                seta   %dl
  402b80:       0f 92 c0                setb   %al
  402b83:       38 c2                   cmp    %al,%dl
  402b85:       0f 85 47 ff ff ff       jne    402ad2 <submitr+0x50c>
  402b8b:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402b92:       00
  402b93:       48 8d 7c 24 40          lea    0x40(%rsp),%rdi
  402b98:       ba 00 20 00 00          mov    $0x2000,%edx
  402b9d:       e8 6b f8 ff ff          callq  40240d <rio_readlineb>
  402ba2:       48 85 c0                test   %rax,%rax
  402ba5:       0f 8f 83 00 00 00       jg     402c2e <submitr+0x668>
  402bab:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402bb2:       3a 20 43
  402bb5:       48 89 03                mov    %rax,(%rbx)
  402bb8:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402bbf:       20 75 6e
  402bc2:       48 89 43 08             mov    %rax,0x8(%rbx)
  402bc6:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402bcd:       74 6f 20
  402bd0:       48 89 43 10             mov    %rax,0x10(%rbx)
  402bd4:       48 b8 72 65 61 64 20    movabs $0x6174732064616572,%rax
  402bdb:       73 74 61
  402bde:       48 89 43 18             mov    %rax,0x18(%rbx)
  402be2:       48 b8 74 75 73 20 6d    movabs $0x7373656d20737574,%rax
  402be9:       65 73 73
  402bec:       48 89 43 20             mov    %rax,0x20(%rbx)
  402bf0:       48 b8 61 67 65 20 66    movabs $0x6d6f726620656761,%rax
  402bf7:       72 6f 6d
  402bfa:       48 89 43 28             mov    %rax,0x28(%rbx)
  402bfe:       48 b8 20 72 65 73 75    movabs $0x20746c7573657220,%rax
  402c05:       6c 74 20
  402c08:       48 89 43 30             mov    %rax,0x30(%rbx)
  402c0c:       c7 43 38 73 65 72 76    movl   $0x76726573,0x38(%rbx)
  402c13:       66 c7 43 3c 65 72       movw   $0x7265,0x3c(%rbx)
  402c19:       c6 43 3e 00             movb   $0x0,0x3e(%rbx)
  402c1d:       89 ef                   mov    %ebp,%edi
  402c1f:       e8 fc e0 ff ff          callq  400d20 <close@plt>
  402c24:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402c29:       e9 c0 00 00 00          jmpq   402cee <submitr+0x728>
  402c2e:       44 8b 44 24 2c          mov    0x2c(%rsp),%r8d
  402c33:       41 81 f8 c8 00 00 00    cmp    $0xc8,%r8d
  402c3a:       74 36                   je     402c72 <submitr+0x6ac>
  402c3c:       4c 8d 8c 24 50 80 00    lea    0x8050(%rsp),%r9
  402c43:       00
  402c44:       48 8d 0d bd 0b 00 00    lea    0xbbd(%rip),%rcx        # 403808 <trans_char+0x78>
  402c4b:       48 c7 c2 ff ff ff ff    mov    $0xffffffffffffffff,%rdx
  402c52:       be 01 00 00 00          mov    $0x1,%esi
  402c57:       48 89 df                mov    %rbx,%rdi
  402c5a:       b8 00 00 00 00          mov    $0x0,%eax
  402c5f:       e8 fc e1 ff ff          callq  400e60 <__sprintf_chk@plt>
  402c64:       89 ef                   mov    %ebp,%edi
  402c66:       e8 b5 e0 ff ff          callq  400d20 <close@plt>
  402c6b:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402c70:       eb 7c                   jmp    402cee <submitr+0x728>
  402c72:       48 8d b4 24 50 20 00    lea    0x2050(%rsp),%rsi
  402c79:       00
  402c7a:       48 89 df                mov    %rbx,%rdi
  402c7d:       e8 2e e0 ff ff          callq  400cb0 <strcpy@plt>
  402c82:       89 ef                   mov    %ebp,%edi
  402c84:       e8 97 e0 ff ff          callq  400d20 <close@plt>
  402c89:       b9 04 00 00 00          mov    $0x4,%ecx
  402c8e:       48 8d 3d bb 0b 00 00    lea    0xbbb(%rip),%rdi        # 403850 <trans_char+0xc0>
  402c95:       48 89 de                mov    %rbx,%rsi
  402c98:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402c9a:       0f 97 c0                seta   %al
  402c9d:       0f 92 c2                setb   %dl
  402ca0:       29 d0                   sub    %edx,%eax
  402ca2:       0f be c0                movsbl %al,%eax
  402ca5:       85 c0                   test   %eax,%eax
  402ca7:       74 45                   je     402cee <submitr+0x728>
  402ca9:       b9 05 00 00 00          mov    $0x5,%ecx
  402cae:       48 8d 3d 9f 0b 00 00    lea    0xb9f(%rip),%rdi        # 403854 <trans_char+0xc4>
  402cb5:       48 89 de                mov    %rbx,%rsi
  402cb8:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402cba:       0f 97 c0                seta   %al
  402cbd:       0f 92 c2                setb   %dl
  402cc0:       29 d0                   sub    %edx,%eax
  402cc2:       0f be c0                movsbl %al,%eax
  402cc5:       85 c0                   test   %eax,%eax
  402cc7:       74 25                   je     402cee <submitr+0x728>
  402cc9:       b9 03 00 00 00          mov    $0x3,%ecx
  402cce:       48 8d 3d 84 0b 00 00    lea    0xb84(%rip),%rdi        # 403859 <trans_char+0xc9>
  402cd5:       48 89 de                mov    %rbx,%rsi
  402cd8:       f3 a6                   repz cmpsb %es:(%rdi),%ds:(%rsi)
  402cda:       0f 97 c0                seta   %al
  402cdd:       0f 92 c2                setb   %dl
  402ce0:       29 d0                   sub    %edx,%eax
  402ce2:       0f be c0                movsbl %al,%eax
  402ce5:       85 c0                   test   %eax,%eax
  402ce7:       74 05                   je     402cee <submitr+0x728>
  402ce9:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402cee:       48 8b 9c 24 58 a0 00    mov    0xa058(%rsp),%rbx
  402cf5:       00
  402cf6:       64 48 33 1c 25 28 00    xor    %fs:0x28,%rbx
  402cfd:       00 00
  402cff:       74 05                   je     402d06 <submitr+0x740>
  402d01:       e8 da df ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402d06:       48 81 c4 68 a0 00 00    add    $0xa068,%rsp
  402d0d:       5b                      pop    %rbx
  402d0e:       5d                      pop    %rbp
  402d0f:       41 5c                   pop    %r12
  402d11:       41 5d                   pop    %r13
  402d13:       41 5e                   pop    %r14
  402d15:       41 5f                   pop    %r15
  402d17:       c3                      retq

0000000000402d18 <init_timeout>:
  402d18:       85 ff                   test   %edi,%edi
  402d1a:       74 25                   je     402d41 <init_timeout+0x29>
  402d1c:       53                      push   %rbx
  402d1d:       89 fb                   mov    %edi,%ebx
  402d1f:       85 ff                   test   %edi,%edi
  402d21:       79 05                   jns    402d28 <init_timeout+0x10>
  402d23:       bb 00 00 00 00          mov    $0x0,%ebx
  402d28:       48 8d 35 c7 f5 ff ff    lea    -0xa39(%rip),%rsi        # 4022f6 <sigalrm_handler>
  402d2f:       bf 0e 00 00 00          mov    $0xe,%edi
  402d34:       e8 07 e0 ff ff          callq  400d40 <signal@plt>
  402d39:       89 df                   mov    %ebx,%edi
  402d3b:       e8 d0 df ff ff          callq  400d10 <alarm@plt>
  402d40:       5b                      pop    %rbx
  402d41:       f3 c3                   repz retq

0000000000402d43 <init_driver>:
  402d43:       41 54                   push   %r12
  402d45:       55                      push   %rbp
  402d46:       53                      push   %rbx
  402d47:       48 83 ec 20             sub    $0x20,%rsp
  402d4b:       48 89 fd                mov    %rdi,%rbp
  402d4e:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
  402d55:       00 00
  402d57:       48 89 44 24 18          mov    %rax,0x18(%rsp)
  402d5c:       31 c0                   xor    %eax,%eax
  402d5e:       be 01 00 00 00          mov    $0x1,%esi
  402d63:       bf 0d 00 00 00          mov    $0xd,%edi
  402d68:       e8 d3 df ff ff          callq  400d40 <signal@plt>
  402d6d:       be 01 00 00 00          mov    $0x1,%esi
  402d72:       bf 1d 00 00 00          mov    $0x1d,%edi
  402d77:       e8 c4 df ff ff          callq  400d40 <signal@plt>
  402d7c:       be 01 00 00 00          mov    $0x1,%esi
  402d81:       bf 1d 00 00 00          mov    $0x1d,%edi
  402d86:       e8 b5 df ff ff          callq  400d40 <signal@plt>
  402d8b:       ba 00 00 00 00          mov    $0x0,%edx
  402d90:       be 01 00 00 00          mov    $0x1,%esi
  402d95:       bf 02 00 00 00          mov    $0x2,%edi
  402d9a:       e8 d1 e0 ff ff          callq  400e70 <socket@plt>
  402d9f:       85 c0                   test   %eax,%eax
  402da1:       79 4f                   jns    402df2 <init_driver+0xaf>
  402da3:       48 b8 45 72 72 6f 72    movabs $0x43203a726f727245,%rax
  402daa:       3a 20 43
  402dad:       48 89 45 00             mov    %rax,0x0(%rbp)
  402db1:       48 b8 6c 69 65 6e 74    movabs $0x6e7520746e65696c,%rax
  402db8:       20 75 6e
  402dbb:       48 89 45 08             mov    %rax,0x8(%rbp)
  402dbf:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402dc6:       74 6f 20
  402dc9:       48 89 45 10             mov    %rax,0x10(%rbp)
  402dcd:       48 b8 63 72 65 61 74    movabs $0x7320657461657263,%rax
  402dd4:       65 20 73
  402dd7:       48 89 45 18             mov    %rax,0x18(%rbp)
  402ddb:       c7 45 20 6f 63 6b 65    movl   $0x656b636f,0x20(%rbp)
  402de2:       66 c7 45 24 74 00       movw   $0x74,0x24(%rbp)
  402de8:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402ded:       e9 2c 01 00 00          jmpq   402f1e <init_driver+0x1db>
  402df2:       89 c3                   mov    %eax,%ebx
  402df4:       48 8d 3d 61 0a 00 00    lea    0xa61(%rip),%rdi        # 40385c <trans_char+0xcc>
  402dfb:       e8 50 df ff ff          callq  400d50 <gethostbyname@plt>
  402e00:       48 85 c0                test   %rax,%rax
  402e03:       75 68                   jne    402e6d <init_driver+0x12a>
  402e05:       48 b8 45 72 72 6f 72    movabs $0x44203a726f727245,%rax
  402e0c:       3a 20 44
  402e0f:       48 89 45 00             mov    %rax,0x0(%rbp)
  402e13:       48 b8 4e 53 20 69 73    movabs $0x6e7520736920534e,%rax
  402e1a:       20 75 6e
  402e1d:       48 89 45 08             mov    %rax,0x8(%rbp)
  402e21:       48 b8 61 62 6c 65 20    movabs $0x206f7420656c6261,%rax
  402e28:       74 6f 20
  402e2b:       48 89 45 10             mov    %rax,0x10(%rbp)
  402e2f:       48 b8 72 65 73 6f 6c    movabs $0x2065766c6f736572,%rax
  402e36:       76 65 20
  402e39:       48 89 45 18             mov    %rax,0x18(%rbp)
  402e3d:       48 b8 73 65 72 76 65    movabs $0x6120726576726573,%rax
  402e44:       72 20 61
  402e47:       48 89 45 20             mov    %rax,0x20(%rbp)
  402e4b:       c7 45 28 64 64 72 65    movl   $0x65726464,0x28(%rbp)
  402e52:       66 c7 45 2c 73 73       movw   $0x7373,0x2c(%rbp)
  402e58:       c6 45 2e 00             movb   $0x0,0x2e(%rbp)
  402e5c:       89 df                   mov    %ebx,%edi
  402e5e:       e8 bd de ff ff          callq  400d20 <close@plt>
  402e63:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402e68:       e9 b1 00 00 00          jmpq   402f1e <init_driver+0x1db>
  402e6d:       48 c7 04 24 00 00 00    movq   $0x0,(%rsp)
  402e74:       00
  402e75:       48 c7 44 24 08 00 00    movq   $0x0,0x8(%rsp)
  402e7c:       00 00
  402e7e:       66 c7 04 24 02 00       movw   $0x2,(%rsp)
  402e84:       48 63 50 14             movslq 0x14(%rax),%rdx
  402e88:       48 8b 40 18             mov    0x18(%rax),%rax
  402e8c:       48 8b 30                mov    (%rax),%rsi
  402e8f:       48 8d 7c 24 04          lea    0x4(%rsp),%rdi
  402e94:       b9 0c 00 00 00          mov    $0xc,%ecx
  402e99:       e8 c2 de ff ff          callq  400d60 <__memmove_chk@plt>
  402e9e:       66 c7 44 24 02 4b 79    movw   $0x794b,0x2(%rsp)
  402ea5:       ba 10 00 00 00          mov    $0x10,%edx
  402eaa:       48 89 e6                mov    %rsp,%rsi
  402ead:       89 df                   mov    %ebx,%edi
  402eaf:       e8 8c df ff ff          callq  400e40 <connect@plt>
  402eb4:       85 c0                   test   %eax,%eax
  402eb6:       79 50                   jns    402f08 <init_driver+0x1c5>
  402eb8:       48 b8 45 72 72 6f 72    movabs $0x55203a726f727245,%rax
  402ebf:       3a 20 55
  402ec2:       48 89 45 00             mov    %rax,0x0(%rbp)
  402ec6:       48 b8 6e 61 62 6c 65    movabs $0x6f7420656c62616e,%rax
  402ecd:       20 74 6f
  402ed0:       48 89 45 08             mov    %rax,0x8(%rbp)
  402ed4:       48 b8 20 63 6f 6e 6e    movabs $0x7463656e6e6f6320,%rax
  402edb:       65 63 74
  402ede:       48 89 45 10             mov    %rax,0x10(%rbp)
  402ee2:       48 b8 20 74 6f 20 73    movabs $0x76726573206f7420,%rax
  402ee9:       65 72 76
  402eec:       48 89 45 18             mov    %rax,0x18(%rbp)
  402ef0:       66 c7 45 20 65 72       movw   $0x7265,0x20(%rbp)
  402ef6:       c6 45 22 00             movb   $0x0,0x22(%rbp)
  402efa:       89 df                   mov    %ebx,%edi
  402efc:       e8 1f de ff ff          callq  400d20 <close@plt>
  402f01:       b8 ff ff ff ff          mov    $0xffffffff,%eax
  402f06:       eb 16                   jmp    402f1e <init_driver+0x1db>
  402f08:       89 df                   mov    %ebx,%edi
  402f0a:       e8 11 de ff ff          callq  400d20 <close@plt>
  402f0f:       66 c7 45 00 4f 4b       movw   $0x4b4f,0x0(%rbp)
  402f15:       c6 45 02 00             movb   $0x0,0x2(%rbp)
  402f19:       b8 00 00 00 00          mov    $0x0,%eax
  402f1e:       48 8b 4c 24 18          mov    0x18(%rsp),%rcx
  402f23:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
  402f2a:       00 00
  402f2c:       74 05                   je     402f33 <init_driver+0x1f0>
  402f2e:       e8 ad dd ff ff          callq  400ce0 <__stack_chk_fail@plt>
  402f33:       48 83 c4 20             add    $0x20,%rsp
  402f37:       5b                      pop    %rbx
  402f38:       5d                      pop    %rbp
  402f39:       41 5c                   pop    %r12
  402f3b:       c3                      retq

0000000000402f3c <driver_post>:
  402f3c:       53                      push   %rbx
  402f3d:       4c 89 cb                mov    %r9,%rbx
  402f40:       45 85 c0                test   %r8d,%r8d
  402f43:       74 29                   je     402f6e <driver_post+0x32>
  402f45:       48 89 ca                mov    %rcx,%rdx
  402f48:       48 8d 35 1c 09 00 00    lea    0x91c(%rip),%rsi        # 40386b <trans_char+0xdb>
  402f4f:       bf 01 00 00 00          mov    $0x1,%edi
  402f54:       b8 00 00 00 00          mov    $0x0,%eax
  402f59:       e8 82 de ff ff          callq  400de0 <__printf_chk@plt>
  402f5e:       66 c7 03 4f 4b          movw   $0x4b4f,(%rbx)
  402f63:       c6 43 02 00             movb   $0x0,0x2(%rbx)
  402f67:       b8 00 00 00 00          mov    $0x0,%eax
  402f6c:       eb 41                   jmp    402faf <driver_post+0x73>
  402f6e:       48 85 ff                test   %rdi,%rdi
  402f71:       74 2e                   je     402fa1 <driver_post+0x65>
  402f73:       80 3f 00                cmpb   $0x0,(%rdi)
  402f76:       74 29                   je     402fa1 <driver_post+0x65>
  402f78:       48 83 ec 08             sub    $0x8,%rsp
  402f7c:       41 51                   push   %r9
  402f7e:       49 89 c9                mov    %rcx,%r9
  402f81:       49 89 d0                mov    %rdx,%r8
  402f84:       48 89 f9                mov    %rdi,%rcx
  402f87:       48 89 f2                mov    %rsi,%rdx
  402f8a:       be 79 4b 00 00          mov    $0x4b79,%esi
  402f8f:       48 8d 3d c6 08 00 00    lea    0x8c6(%rip),%rdi        # 40385c <trans_char+0xcc>
  402f96:       e8 2b f6 ff ff          callq  4025c6 <submitr>
  402f9b:       48 83 c4 10             add    $0x10,%rsp
  402f9f:       eb 0e                   jmp    402faf <driver_post+0x73>
  402fa1:       66 c7 03 4f 4b          movw   $0x4b4f,(%rbx)
  402fa6:       c6 43 02 00             movb   $0x0,0x2(%rbx)
  402faa:       b8 00 00 00 00          mov    $0x0,%eax
  402faf:       5b                      pop    %rbx
  402fb0:       c3                      retq

0000000000402fb1 <check>:
  402fb1:       89 f8                   mov    %edi,%eax
  402fb3:       c1 e8 1c                shr    $0x1c,%eax
  402fb6:       85 c0                   test   %eax,%eax
  402fb8:       74 1d                   je     402fd7 <check+0x26>
  402fba:       b9 00 00 00 00          mov    $0x0,%ecx
  402fbf:       eb 0b                   jmp    402fcc <check+0x1b>
  402fc1:       89 f8                   mov    %edi,%eax
  402fc3:       d3 e8                   shr    %cl,%eax
  402fc5:       3c 0a                   cmp    $0xa,%al
  402fc7:       74 14                   je     402fdd <check+0x2c>
  402fc9:       83 c1 08                add    $0x8,%ecx
  402fcc:       83 f9 1f                cmp    $0x1f,%ecx
  402fcf:       7e f0                   jle    402fc1 <check+0x10>
  402fd1:       b8 01 00 00 00          mov    $0x1,%eax
  402fd6:       c3                      retq
  402fd7:       b8 00 00 00 00          mov    $0x0,%eax
  402fdc:       c3                      retq
  402fdd:       b8 00 00 00 00          mov    $0x0,%eax
  402fe2:       c3                      retq

0000000000402fe3 <gencookie>:
  402fe3:       53                      push   %rbx
  402fe4:       83 c7 01                add    $0x1,%edi
  402fe7:       e8 a4 dc ff ff          callq  400c90 <srandom@plt>
  402fec:       e8 af dd ff ff          callq  400da0 <random@plt>
  402ff1:       89 c3                   mov    %eax,%ebx
  402ff3:       89 c7                   mov    %eax,%edi
  402ff5:       e8 b7 ff ff ff          callq  402fb1 <check>
  402ffa:       85 c0                   test   %eax,%eax
  402ffc:       74 ee                   je     402fec <gencookie+0x9>
  402ffe:       89 d8                   mov    %ebx,%eax
  403000:       5b                      pop    %rbx
  403001:       c3                      retq
  403002:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  403009:       00 00 00
  40300c:       0f 1f 40 00             nopl   0x0(%rax)

0000000000403010 <__libc_csu_init>:
  403010:       41 57                   push   %r15
  403012:       41 56                   push   %r14
  403014:       49 89 d7                mov    %rdx,%r15
  403017:       41 55                   push   %r13
  403019:       41 54                   push   %r12
  40301b:       4c 8d 25 e6 1d 20 00    lea    0x201de6(%rip),%r12        # 604e08 <__frame_dummy_init_array_entry>
  403022:       55                      push   %rbp
  403023:       48 8d 2d e6 1d 20 00    lea    0x201de6(%rip),%rbp        # 604e10 <__init_array_end>
  40302a:       53                      push   %rbx
  40302b:       41 89 fd                mov    %edi,%r13d
  40302e:       49 89 f6                mov    %rsi,%r14
  403031:       4c 29 e5                sub    %r12,%rbp
  403034:       48 83 ec 08             sub    $0x8,%rsp
  403038:       48 c1 fd 03             sar    $0x3,%rbp
  40303c:       e8 07 dc ff ff          callq  400c48 <_init>
  403041:       48 85 ed                test   %rbp,%rbp
  403044:       74 20                   je     403066 <__libc_csu_init+0x56>
  403046:       31 db                   xor    %ebx,%ebx
  403048:       0f 1f 84 00 00 00 00    nopl   0x0(%rax,%rax,1)
  40304f:       00
  403050:       4c 89 fa                mov    %r15,%rdx
  403053:       4c 89 f6                mov    %r14,%rsi
  403056:       44 89 ef                mov    %r13d,%edi
  403059:       41 ff 14 dc             callq  *(%r12,%rbx,8)
  40305d:       48 83 c3 01             add    $0x1,%rbx
  403061:       48 39 dd                cmp    %rbx,%rbp
  403064:       75 ea                   jne    403050 <__libc_csu_init+0x40>
  403066:       48 83 c4 08             add    $0x8,%rsp
  40306a:       5b                      pop    %rbx
  40306b:       5d                      pop    %rbp
  40306c:       41 5c                   pop    %r12
  40306e:       41 5d                   pop    %r13
  403070:       41 5e                   pop    %r14
  403072:       41 5f                   pop    %r15
  403074:       c3                      retq
  403075:       90                      nop
  403076:       66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
  40307d:       00 00 00

0000000000403080 <__libc_csu_fini>:
  403080:       f3 c3                   repz retq

Disassembly of section .fini:

0000000000403084 <_fini>:
  403084:       48 83 ec 08             sub    $0x8,%rsp
  403088:       48 83 c4 08             add    $0x8,%rsp
  40308c:       c3                      retq