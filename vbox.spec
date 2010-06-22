Name: vbox
Version: 1.0
Release: alt11
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


%prep
%setup

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot/var/lib/vbox/
install -m755 vbox-client/bin/* %buildroot%_bindir/
install -m755 vbox-server/bin/* %buildroot%_bindir/
cp -ar vbox-server/etc/* %buildroot%_sysconfdir/


%pre server
%groupadd vboxusers ||:
%useradd -G vboxusers -d /var/lib/vbox -c "VirtualBox User" vboxuser ||:


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
%attr(0755,root,root) %_initdir/vboxmachines
%dir /var/lib/vbox/
%attr(0700,vboxuser,vboxuser) /var/lib/vbox/


%changelog
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

