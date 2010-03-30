Name: vbox
Version: 1.0
Release: alt1

Summary: Etersoft's scripts for testing in remote VirtualBox machines
License: GPL
Group: Communications
Url: http://wiki.office.etersoft.ru/testing/virtualbox

Packager: Devaev Maxim <mdevaev@etersoft.ru>

# git.eter:/people/mdevaev/packages/vbox.git
Source: %name-%version.tar
BuildArchitectures: noarch
#AutoReq: no

%description
Etersoft's scripts for testing in remote VirtualBox machines

##### Client #####
%package client
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: Communications

%description client
Client for remote virtualbox machines

##### Server #####
%package server
Summary: Etersoft's scripts for testing in remote VirtualBox machines
Group: Communications

%description server
Server of remote virtualbox machines


##### Common inst #####
%prep
%setup

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir
chmod a+rx vbox-client/bin/*
chmod a+rx vbox-server/bin/*
cp vbox-client/bin/* %buildroot%_bindir/
cp vbox-server/bin/* %buildroot%_bindir/
cp -ar vbox-server/etc/* %buildroot%_sysconfdir/

##### Client #####
%files client
%_bindir/vbox

##### Server #####
%files server
%_bindir/VBoxShared
%attr(0400,root,root) %_sysconfdir/sudo.d/vbox
%_sysconfdir/vbox/vbox.conf
%_sysconfdir/vbox/vbox.nxs
%_sysconfdir/vbox/vboxmachines.conf
%_sysconfdir/vbox/vboxmachines.list
%attr(0755,root,root) %_sysconfdir/init.d/vboxmachines


##### Changelog #####
%changelog
* Tue Mar 30 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build

