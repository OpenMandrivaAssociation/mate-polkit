%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	1
%define	major	0
%define	gimajor	%{api}.0
%define	libname	%mklibname polkit-gtk-mate %{api} %{major}
%define	girname	%mklibname polkitgtkmate-gir %{gimajor}
%define	devname	%mklibname polkit-gtk-mate -d

Summary:	PolicyKit integration for the MATE desktop
Name:		mate-polkit
Version:	1.18.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	polkit-gnome-authentication-agent-1.desktop.in
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(polkit-agent-1)
Provides:	polkit-agent
Provides:	polkit-mate = %{EVRD}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides an Authentication Agent for PolicyKit that integrates
well with the MATE desktop environment

%files -f %{name}.lang
%doc COPYING AUTHORS README
%config(noreplace) %{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Development files for polkit-mate
Group:		System/Libraries

%description -n %{libname}
Development files for %{name}.

%files -n %{libname}
%{_libdir}/libpolkit-gtk-mate-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/PolkitGtkMate-%{gimajor}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for polkit-mate
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/polkit-gtk-mate-1
%dir %{_includedir}/polkit-gtk-mate-1/polkitgtkmate
%{_includedir}/polkit-gtk-mate-1/polkitgtkmate/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/polkit-gtk-mate-%{api}.pc
%{_datadir}/gir-1.0/PolkitGtkMate-%{gimajor}.gir

#----------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-gtk-doc-html \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

