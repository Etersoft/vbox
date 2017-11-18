# since rpm-build-intro 1.7.25
%define _sudoersdir %_sysconfdir/sudoers.d

Name: vbox
Version: 1.6
Release: alt1

Summary: Etersoft's scripts for testing in remote VirtualBox machines

License: GPL
Group: Communications
Url: http://wiki.office.etersoft.ru/testing/virtualbox

Packager: Devaev Maxim <mdevaev@etersoft.ru>

#Git: http://git.etersoft.ru/people/mdevaev/packages/vbox.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-intro

%description
Etersoft's scripts for testing in remote VirtualBox machines.

%package client
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: Communications
%description client
Client for remote virtualbox machines.

Requires: opennx


%package server
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: Communications
%description server
Server of remote virtualbox machines.


%package dhcpinfo
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: System/Servers
%description dhcpinfo
Special ssh user for issue dhcp information


%prep
%setup


%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/
mkdir -p %buildroot%_sudoersdir/
mkdir -p %buildroot%_initdir/
mkdir -p %buildroot%_var/lib/vbox/
mkdir -p %buildroot%_var/lib/dhcpinfo/

install -m755 vbox-client/bin/* %buildroot%_bindir/
install -m755 vbox-server/bin/* %buildroot%_bindir/
install -m755 vbox-dhcpinfo/bin/* %buildroot%_bindir/

install -m755 vbox-server/etc/rc.d/init.d/vboxmachines %buildroot%_initdir/
cp -ar vbox-server/etc/sudoers.d/* %buildroot%_sudoersdir/
cp -ar vbox-server/etc/vbox %buildroot%_sysconfdir/
cp -ar vbox-dhcpinfo/etc/* %buildroot%_sysconfdir/
cp -ar vbox-dhcpinfo/var/* %buildroot%_var/


%pre server
%groupadd vboxusers ||:
%useradd -g vboxusers -d /var/lib/vbox -c "VirtualBox User" vboxuser ||:


%pre dhcpinfo
%groupadd dhcpinfo ||:
%useradd -g dhcpinfo -c "DHCP information issue" -s %_bindir/dhcpinfo -d /var/lib/dhcpinfo dhcpinfo ||:


%files client
%_bindir/vbox


%files server
%_bindir/VBoxShared
%attr(0400,root,root) %_sudoersdir/vbox
%dir %_sysconfdir/vbox/
%dir %_sysconfdir/vbox/vboxmachines.d/
%dir %_sysconfdir/vbox/scripts/
%dir %_sysconfdir/vbox/scripts/groupmachines
%config(noreplace) %_sysconfdir/vbox/vbox.conf
%config(noreplace) %_sysconfdir/vbox/vbox.nxs
%config(noreplace) %_sysconfdir/vbox/vboxmachines.conf
%config(noreplace) %_sysconfdir/vbox/vboxmachines.list
%config(noreplace) %_sysconfdir/vbox/vboxmachines.d/*.list
%config(noreplace) %_sysconfdir/vbox/vboxmachines.d/*.conf
%config(noreplace) %_sysconfdir/vbox/scripts/vm*
%config(noreplace) %_sysconfdir/vbox/scripts/*/vm*
%config(noreplace) %_sysconfdir/vbox/scripts/*/group*
%attr(0600,vboxuser,vboxusers) %_sysconfdir/vbox/dhcpinfo.key
%_initdir/vboxmachines
%dir /var/lib/vbox/
%attr(0700,vboxuser,vboxusers) /var/lib/vbox/


%files dhcpinfo
%_bindir/dhcpinfo
%config(noreplace) %_sysconfdir/dhcpinfo.conf
%_var/lib/dhcpinfo/


%changelog
* Sat Nov 18 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- vbox: add --autologin

* Wed Sep 04 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.5-alt1
- Add VBOX_GROUP_GLOBAL_START flag for choice of VM start at service startup
- Empty machine lists are treated without errors while status command now

* Mon Feb 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- added --snapshot to /bin/vbox

* Mon Feb 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- pack sudoers file to /etc/sudoers.d via _sudoersdir macro (fix eterbug #9078)
- use opennx by default

* Thu Nov 10 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.2-alt2
- Pack /etc/vbox/scripts/groupmachines directory due
  sisyphus_check: subdirectories packaging violation

* Tue Oct 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.2-alt1
- Add group machines support

* Fri Mar 18 2011 Denis Baranov <baraka@altlinux.ru> 1.1-alt7
- Add new adress dhcp-server

* Sat Mar 05 2011 Denis Baranov <baraka@altlinux.ru> 1.1-alt6
- Add path to VirtualBox in vbox.conf

* Sat Mar 05 2011 Denis Baranov <baraka@altlinux.ru> 1.1-alt5
- cleanup spec and new build
- do not autoreq VirtualBox

* Sat Mar 05 2011 Denis Baranov <baraka@altlinux.ru> 1.1-alt4
- Add option vbox --reset
- Get list vms on server

* Tue Jul 13 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt3
- Fixed dhcpinfo user creation

* Tue Jul 12 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt2
- Auto checks host key

* Mon Jul 12 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt1
- Added fake login shell, issue DHCP information over SSH
- Fixed group creating
- Fixed home folder for dhcpinfo user to /dev/null
- DSA key authentication for dhcpinfo

* Tue Jun 22 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt12
- Changed default DHCP config path

* Thu May 20 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt11
- Ssh-agent detecting by SSH_AUTH_SOCK

* Wed May 05 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt10
- Fixed missing directory /var/lib/vbox

* Wed May 05 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt9
- Fixed vboxuser home path

* Wed May 05 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt8
- Fixed vboxuser creation

* Thu Apr 29 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt7
- Added ssh-agent test

* Thu Apr 22 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt6
- Actual help information

* Thu Apr 22 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt5
- Added state column, info command, ACPI poweroff command

* Sat Apr 03 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt4
- Added copyright info

* Sat Apr 03 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt3
- Removed -r option from useradd macro

* Sat Apr 03 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt2
- Added BuildRequires: rpm-build-compat

* Tue Mar 30 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build

