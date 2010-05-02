Name: qacdp
Summary: A QT frontend for ACDP
Version: 0.1.0
Release: %mkrel 2
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
