%define	name	enna
%define	version	0.3.0
%define release %mkrel 4

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Media center
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	e16-like
Group: 		Graphical desktop/Enlightenment
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.digital-corner.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRequires:  evas-devel >= 0.9.9.052
BuildRequires:  ecore-devel >= 0.9.9.050
BuildRequires:  edje-devel >= 0.5.0.050
BuildRequires:	e_dbus-devel >= 0.5.0.050
BuildRequires:  lirc-devel
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:	edje >= 0.9.9.050,  embryo >= 0.9.9.050
Buildrequires:	gettext-devel
Requires:	xmms2
Requires:	mplayer
Requires:	xine-ui

%description
A media center based on the Enlightenment libraries.

%prep
%setup -q -n %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

rm -f %buildroot%{_libdir}/%name/modules/*.{a,la}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/%name/modules/*.so
%{_datadir}/applications/%{name}.desktop
