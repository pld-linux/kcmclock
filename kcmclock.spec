Summary:	A kcontrol modules to change the Date & Time of your system
Summary(pl):	Modu³ kontrolny do zmieniania daty i czau systemowego
Name:		kcmclock
Version:	0.1
Release:	3
Copyright:	GPL
Source:		%{name}-%{version}.tgz
Group:		X11/KDE
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A kcontrol module that allow you to change the Date & Time of your Linux Box
( previously was a kclock built-in dialog ).

Copyright (C) 1998 Luca Montecchiani <[1]m.luca@usa.net>

%description -l pl
Modu³ dla kcontrol pozwalaj±cy na zmianê Daty oraz Czasu.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/doc/HTML/default/kcontrol/kcmclock
/usr/X11R6/share/applnk/Settings/kcmclock.kdelnk
/usr/X11R6/share/icons/kcmclock.xpm
