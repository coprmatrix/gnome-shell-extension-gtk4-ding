Name:           gnome-shell-extension-gtk4-ding
Version:        47.0.5
Release:        1
Summary:        A fork from the official desktop icons project
License:        GPL-3.0-or-later
Url:            https://gitlab.com/rastersoft/desktop-icons-ng
Source0:        desktop-icons-ng-%{version}.tar.xz

# Meson and Ninja BuildRequires
BuildRequires:  meson
BuildRequires:  (ninja or ninja-build)
BuildRequires:  glib2-devel
BuildRequires:  fdupes
BuildArch:      noarch

%description
A fork from the official desktop icons project, with several enhancements like Drag'n'Drop.

%prep
%setup -q -n desktop-icons-ng-%{version}

%build
meson --prefix=%{_prefix} --localedir=%{_datadir}/gnome-shell/extensions/ding@rastersoft.com/locale .build
ninja -C .build

%install
DESTDIR=%{buildroot} ninja -C .build install

# Copy built extension to appropriate directory
install -d %{buildroot}%{_datadir}/gnome-shell/extensions/ding@rastersoft.com
cp -r * %{buildroot}%{_datadir}/gnome-shell/extensions/ding@rastersoft.com/

%fdupes %{buildroot}%{_datadir}

%files
%doc README.md
%dir /etc/apparmor.d
/etc/apparmor.d/gtk4-desktop-icons
%{_datadir}/gnome-shell/extensions/ding@rastersoft.com
%{_datadir}/gnome-shell/extensions/gtk4-ding@smedius.gitlab.com
%{_datadir}/glib-2.0/schemas/*

%changelog
