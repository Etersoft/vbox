Name: vbox
Version: 1.1
Release: alt2
Summary: Etersoft's scripts for testing in remote VirtualBox machines
License: GPL
Group: Communications
Url: http://wiki.office.etersoft.ru/testing/virtualbox
Packager: Devaev Maxim <mdevaev@etersoft.ru>
#Git: http://git.etersoft.ru/people/mdevaev/packages/vbox.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: rpm-build-compat
%description
Etersoft's scripts for testing in remote VirtualBox machines.


%package client
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: Communications
%description client
Client for remote virtualbox machines.


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
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_var/lib/vbox/
mkdir -p %buildroot%_var/lib/dhcpinfo/
install -m755 vbox-client/bin/* %buildroot%_bindir/
install -m755 vbox-server/bin/* %buildroot%_bindir/
install -m755 vbox-dhcpinfo/bin/* %buildroot%_bindir/
cp -ar vbox-server/etc/* %buildroot%_sysconfdir/
cp -ar vbox-dhcpinfo/etc/* %buildroot%_sysconfdir/
cp -ar vbox-dhcpinfo/var/* %buildroot%_var/


%pre server
%groupadd vboxusers ||:
%useradd -g vboxusers -d /var/lib/vbox -c "VirtualBox User" vboxuser ||:


%pre dhcpinfo
%groupadd dhcpinfo ||:
%useradd -g dhcpinfo -c "DHCP information issue" -s %_bindir/dhcpinfo -b /dev/null dhcpinfo ||:


%files client
%_bindir/vbox


%files server
%_bindir/VBoxShared
%attr(0400,root,root) %_sysconfdir/sudo.d/vbox
%dir %_sysconfdir/vbox/
%config(noreplace) %_sysconfdir/vbox/vbox.conf
%config(noreplace) %_sysconfdir/vbox/vbox.nxs
%config(noreplace) %_sysconfdir/vbox/vboxmachines.conf
%config(noreplace) %_sysconfdir/vbox/vboxmachines.list
%attr(0600,vboxuser,vboxusers) %_sysconfdir/vbox/dhcpinfo.key
%attr(0755,root,root) %_initdir/vboxmachines
%dir /var/lib/vbox/
%attr(0700,vboxuser,vboxuser) /var/lib/vbox/


%files dhcpinfo
%_bindir/dhcpinfo
%config(noreplace) %_sysconfdir/dhcpinfo.conf
%_var/lib/dhcpinfo/


%changelog
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

