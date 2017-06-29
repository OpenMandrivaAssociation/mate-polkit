%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	1
%define	major	0
%define	gimajor	%{api}.0
%define	libname	%mklibname	polkit-gtk-mate %{api} %{major}
%define	girname	%mklibname	polkitgtkmate-gir %{gimajor}
%define	devname	%mklibname	polkit-gtk-mate -d

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
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
Provides:	polkit-agent
Provides:	polkit-mate = %{EVRD}

%description
polkit-mate provides an authentication agent for PolicyKit
that matches the look and feel of the MATE desktop.

%package -n %{libname}
Summary:	Development files for polkit-mate
Group:		System/Libraries

%description -n %{libname}
Development files for polkit-mate.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}

%package -n %{devname}
Summary:	Development files for polkit-mate
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for polkit-mate.

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
sed -i 's,@FULL_LIBEXECDIR@,%{_libdir},' %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS README
%config(noreplace) %{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

%files -n %{libname}
%{_libdir}/libpolkit-gtk-mate-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/PolkitGtkMate-%{gimajor}.typelib

%files -n %{devname}
%dir %{_includedir}/polkit-gtk-mate-1
%dir %{_includedir}/polkit-gtk-mate-1/polkitgtkmate
%{_includedir}/polkit-gtk-mate-1/polkitgtkmate/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/polkit-gtk-mate-%{api}.pc
%{_datadir}/gir-1.0/PolkitGtkMate-%{gimajor}.gir

