%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	1
%define	major	0
%define	libname	%mklibname polkit-gtk-mate %{api} %{major}
%define	devname	%mklibname polkit-gtk-mate -d

%define	gimajor	%{api}.0
%define	girname	%mklibname polkitgtkmate-gir %{gimajor}

Summary:	PolicyKit integration for the MATE desktop
Name:		mate-polkit
Version:	1.26.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	polkit-gnome-authentication-agent-1.desktop.in

BuildRequires:  autoconf-archive
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(polkit-gobject-1)

Requires:       dbus-x11
Requires:       accountsservice

Provides:	polkit-agent
Provides:	polkit-mate = %{EVRD}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides an Authentication Agent for PolicyKit that integrates
well with the MATE desktop environment.

%files -f %{name}.lang
%doc COPYING AUTHORS README
%config(noreplace) %{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name}
