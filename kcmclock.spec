Summary:     A kcontrol modules to change the Date & Time of your system
Summary(pl): Modu³ kontrolny do zmieniania daty i czau systemowego
Name:        kcmclock
Version:     0.1
Release:     3
Copyright:   GPL
Source:      %{name}-%{version}.tgz
Group:       X11/KDE
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A kcontrol module that allow you to change the Date & Time of your Linux Box
( previously was a kclock built-in dialog ).

Copyright (C) 1998 Luca Montecchiani <[1]m.luca@usa.net>

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -Wall" CXXFLAGS="$RPM_OPT_FLAGS -Wall" \
QTINC=/usr/X11R6/include/qt \
./configure %{_target_platform} \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/doc/HTML/default/kcontrol/kcmclock
/usr/X11R6/share/applnk/Settings/kcmclock.kdelnk
/usr/X11R6/share/icons/kcmclock.xpm
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcmclock.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcmclock.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcmclock.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcmclock.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcmclock.mo
%lang(nl) /usr/X11R6/share/locale/pt/LC_MESSAGES/kcmclock.mo
%lang(pt) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcmclock.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcmclock.mo

%changelog
* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1-3]
- KDEDIR changed to /usr/X11R6,
- qt is now placed in /usr/X11R6 also.

* Mon Aug  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.1-2]
- added pl translation,
- added using $RPM_OPT_FLAGS during compilation,
- added devel and static subpackages,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc),
- base dir changed to /usr,
- added -q %setup parameter,
- added %clean section,
- spec rewrited for using Buildroot,
- added using %%{name} and %%{version} macros in Source,
- added %lang macros for %{_datadir}/locale/*/LC_MESSAGES/ files.

* Tue Jun  2 1998 Juergen Helmers <helmerj@rockvax.rockefeller.edu>
  [0.1-1]
- previouse not commented release in rpm package.
