%define	api	1
%define	major	0
%define	girmajor	1.0
%define	libname	%mklibname	polkit-gtk-mate %{api} %{major}
%define	girname	%mklibname	polkitgtkmate-gir %{girmajor}
%define	devname	%mklibname	polkit-gtk-mate -d

Summary:	PolicyKit integration for the MATE desktop
Name:		mate-polkit
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
Source1:	polkit-gnome-authentication-agent-1.desktop.in

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk+-2.0)
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
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for polkit-mate.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
sed -i 's,@FULL_LIBEXECDIR@,%{_libdir},' %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop

%find_lang %{name} --with-mate

%files -f %{name}.lang
%doc COPYING AUTHORS README
%config(noreplace) %{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libexecdir}/polkit-mate-authentication-agent-1

%files -n %{libname}
%{_libdir}/libpolkit-gtk-mate-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/PolkitGtkMate-%{girmajor}.typelib

%files -n %{devname}
%dir %{_includedir}/polkit-gtk-mate-1
%dir %{_includedir}/polkit-gtk-mate-1/polkitgtkmate
%{_includedir}/polkit-gtk-mate-1/polkitgtkmate/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/polkit-gtk-mate-%{api}.pc
%{_datadir}/gir-1.0/PolkitGtkMate-%{girmajor}.gir

