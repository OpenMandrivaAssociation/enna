%define	name	enna
%define	version	0.1.0
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enna is a Emediacenter
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:  evas-devel >= 0.9.9.038, ewl-devel >= 0.5.1.008 
BuildRequires:  ecore-devel >= 0.9.9.038, edje-devel >= 0.5.0.038
BuildRequires:  %{mklibname lirc0}-devel, %{mklibname musicbrainz4}-devel
BuildRequires:  %{mklibname curl4}-devel, %{mklibname taglib0}-devel
BuildRequires:	edje >= 0.5.0.038, e_dbus-devel >= 0.01
Buildrequires:	gettext-devel, emusic-devel, cvs
requires:	xmms2, mplayer, xine-ui

%description
Emedia center

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}
for mo in `ls %buildroot%_datadir/locale/` ;
do Y=`echo -n $mo | sed -e "s|/||"`;
echo "%lang($Y) $(echo %_datadir/locale/${mo}/LC_MESSAGES/%{name}.mo)" >> $RPM_BUILD_DIR/%{name}-%{version}/%{name}.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO ENNARC ENNALIRCRC
%{_bindir}/*
%{_datadir}/%name

