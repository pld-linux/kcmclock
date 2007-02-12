Summary:	A kcontrol modules to change the Date & Time of your system
Summary(pl.UTF-8):   Moduł kontrolny do zmieniania daty i czasu systemowego
Name:		kcmclock
Version:	0.1
Release:	3
Vendor:		Luca Montecchiani <[1]m.luca@usa.net>
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tgz
# Source0-md5:	7aa132a9c54dd4063a5a22bc2c3b3578
#Source0:	http://www.geocities.com/SiliconValley/Vista/2964/kcmclock.tgz
URL:		http://library.cs.tuiasi.ro/kde/apps/kcmclock/
BuildRequires:	kdelibs-devel 
BuildConflicts:	kdelibs-devel > 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A kcontrol module that allow you to change the Date & Time of your
Linux Box ( previously was a kclock built-in dialog ).

%description -l pl.UTF-8
Moduł dla kcontrol pozwalający na zmianę Daty oraz Czasu.

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
