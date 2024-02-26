%define mate_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	PolicyKit integration for the MATE desktop
Name:		mate-polkit
Version:	1.28.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz
Source1:	polkit-gnome-authentication-agent-1.desktop.in

BuildRequires:	autoconf-archive
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(polkit-gobject-1)

Requires:	dbus-x11
Requires:	accountsservice
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
%autosetup -p1

# fix https://github.com/mate-desktop/mate-polkit/issues/56
sed -i '/^Categories=/d' src/polkit-mate-authentication-agent-1.desktop.in
sed -i '/^Categories=/d' src/polkit-mate-authentication-agent-1.desktop.in.in

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--enable-accountsservice \
	--enable-appindicator=yes

%make_build

%install
%make_install

# locales
%find_lang %{name}

