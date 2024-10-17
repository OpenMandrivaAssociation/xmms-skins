%define name xmms-skins
%define version 1.2.10
%define prefix %{_prefix}
%define release %mkrel 1

Name: %{name}
Summary: XMMS - Skins
Version: %{version}
Release: %{release}
License: GPL
URL: https://www.xmms.org/
Source: xmms-skins.tar.bz2
Group: Sound
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



%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.2.10-1mdv2011.0
+ Revision: 645491
- update to new version 1.2.10

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-21mdv2010.0
+ Revision: 435234
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-20mdv2009.0
+ Revision: 262610
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-19mdv2009.0
+ Revision: 257523
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-17mdv2008.1
+ Revision: 130418
- kill re-definition of %%buildroot on Pixel's request
- kill icon tag
- use %%mkrel


* Fri Nov 19 2004 Olivier Blin <blino@mandrake.org> 1.0.0-17mdk
- rebuild

* Sat Sep 13 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-16mdk
- remove possibly offending bmXmms skin, pointed by lenny

* Tue Aug 05 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-15mdk
- don't own /usr/share/xmms/Skins

* Fri May 02 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-14mdk
- rebuild

* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-13mdk
- rebuild to fix invalid-packager

* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-12mdk
- fix obsolete-tag Copyright

* Thu Aug 02 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-11mdk
- update Ayo skin

* Thu Aug 02 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-10mdk
- add Ayo skin

* Thu Jul 05 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-9mdk
- rebuild
- un-dadoustyle-specfile

* Thu Apr 05 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.0-8mdk
- added some nice new skins

* Thu Aug 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-7mdk
- added Packager tag

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-6mdk
- BM
- macros

* Tue Jun 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-5mdk
- added dependency to unzip
- added 4 of the top skins of http://www.xmms.org

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- documentation

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-3mdk
- new groups

* Thu Feb 03 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0.0-2mdk
- split skins into its own rpm spec file; so we can set it to noarch

