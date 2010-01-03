%define	name	enna
%define	version	0.4.0
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Media center
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	e16-like
Group: 		Graphical desktop/Enlightenment
URL:		http://enna.geexbox.org/
Source: 	http://enna.geexbox.org/releases/%{name}-%{version}.tar.bz2
BuildRequires:  evas-devel >= 0.9.9.063
BuildRequires:  ecore-devel >= 0.9.9.063
BuildRequires:	edje >= 0.9.9.063
BuildRequires:  edje-devel >= 0.5.0.0063
BuildRequires:	eet-devel >= 1.2.2
BuildRequires:	embryo >= 0.9.9.063
BuildRequires:	embryo-devel >= 0.9.9.063
BuildRequires:	elementary-devel >= 0.6.0.063
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	libplayer-devel >= 1.0.0
BuildRequires:	libvalhalla-devel >= 1.0.0
Requires:	xmms2
Requires:	mplayer
Requires:	xine-ui
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
A media center based on the Enlightenment libraries.

%prep
%setup -q -n %{name}-%{version}

%build
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
