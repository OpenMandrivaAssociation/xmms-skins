%define name xmms-skins
%define version 1.0.0
%define prefix %{_prefix}
%define release 17mdk

Name: %{name}
Summary: XMMS - Skins
Version: %{version}
Release: %{release}
License: GPL
URL: http://www.xmms.org/
Source: xmms-skins.tar.bz2
Group: Sound
Icon: xmms-skins-logo.xpm
Requires: xmms unzip
Buildroot: %{_tmppath}/%{name}-%{version}
BuildArchitectures: noarch

%description
Skins for xmms. Install this package; at next startup, xmms will see all the
skins. Browse with Options/Skin browser.

If you like skins, please consider installing the package xmms-kjofol-skins
which enables the import of skins for k-jofol.

%prep

%install
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xmms

bzip2 -cd %{SOURCE0} | tar xf - -C $RPM_BUILD_ROOT/%{_datadir}/xmms

cat > README << EOF
This package is a collection of skins for xmms.
Most of them come from http://www.xmms.org
If you would like even more of them you can visit sites like:
  http://www.skinz.org
  http://www.customize.org

If you like skins, please consider installing the package xmms-kjofol-skins
which enable the import of skins for k-jofol.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{_datadir}/xmms/Skins/*

