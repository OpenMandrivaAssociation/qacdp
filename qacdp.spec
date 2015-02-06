Name: qacdp
Summary: A QT frontend for ACDP
Version: 0.1.0
Release: 4
License: GPL
Group: Graphical desktop/KDE
URL: http://www.mandriva.com
Source0:  %{name}-%{version}.tar.bz2
Source1:  qacdp.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: qt4-devel
BuildRequires: cmake

%description
A QT frontend for ACDP

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build
install -m644 -D %{SOURCE1} %{buildroot}/usr/share/applications/qacdp.desktop


%files
%defattr(-,root,root)
%{_bindir}/qacdp
%{_datadir}/applications/qacdp.desktop


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdv2011.0
+ Revision: 614653
- the mass rebuild of 2010.1 packages

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 541550
- fix perm of desktop file

* Tue Apr 27 2010 Alexandre Possebom <alexandre@mandriva.com.br> 0.1.0-1mdv2010.1
+ Revision: 539853
- Changed Group
- First release
- Created package structure for qacdp.

