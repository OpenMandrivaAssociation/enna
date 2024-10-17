%define	name	enna
%define	version	0.4.1
%define release %mkrel 0.2

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Media center
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	e16-like
Group: 		Graphical desktop/Enlightenment
URL:		https://enna.geexbox.org/
Source: 	http://enna.geexbox.org/releases/%{name}-%{version}.tar.xz
BuildRequires:  evas-devel >= 0.9.9.49898
BuildRequires:  ecore-devel >= 0.9.9.49898
BuildRequires:	edje >= 0.9.9.49898
BuildRequires:  edje-devel >= 0.9.9.49898
BuildRequires:	eet-devel >= 1.3.2
BuildRequires:	elementary-devel >= 0.7.0.49898
BuildRequires:	embryo
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	ethumb-devel
BuildRequires:	libplayer-devel >= 2.0.0
BuildRequires:	libvalhalla-devel >= 2.0.0
BuildRequires:	gupnp-av-devel
BuildRequires:	libcddb-devel
BuildRequires:	lirc-devel
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	gettext-devel
BuildRequires:	udev-devel
BuildRequires:	xdg-basedir-devel
BuildRequires:	libxrandr-devel
BuildRequires:	bluez-devel
BuildRequires:	cwiid-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
A media center based on the Enlightenment libraries.

%prep
%setup -q -n %{name}-%{version}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --disable-rpath --disable-static --disable-static-modules
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

rm -f %{buildroot}%{_libdir}/enna/modules/*.la

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/enna/modules/*.so
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_mandir}/man1/enna.1.*
%{_datadir}/applications/%{name}.desktop
