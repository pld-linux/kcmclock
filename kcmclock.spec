Summary:	A kcontrol modules to change the Date & Time of your system
Summary(pl):	Modu³ kontrolny do zmieniania daty i czasu systemowego
Name:		kcmclock
Version:	0.1
Release:	3
License:	GPL
Source0:	%{name}-%{version}.tgz
Group:		X11/KDE
Group(de):	X11/KDE
Group(pl):	X11/KDE
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A kcontrol module that allow you to change the Date & Time of your
Linux Box ( previously was a kclock built-in dialog ).

Copyright (C) 1998 Luca Montecchiani <[1]m.luca@usa.net>

%description -l pl
Modu³ dla kcontrol pozwalaj±cy na zmianê Daty oraz Czasu.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -Wall" CXXFLAGS="%{rpmcflags} -Wall" \
QTINC=%{_includedir}/qt \
./configure %{_target_platform} \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/doc/HTML/default/kcontrol/kcmclock
%{_applnkdir}/Settings/kcmclock.kdelnk
%{_datadir}/icons/kcmclock.xpm
