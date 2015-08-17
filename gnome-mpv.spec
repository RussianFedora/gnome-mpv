Name:           gnome-mpv
Version:        0.5
Release:        1%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPLv3+
URL:            https://github.com/gnome-mpv/gnome-mpv
Source0:        https://github.com/gnome-mpv/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(mpv)
BuildRequires:  python2-devel
# check
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       youtube-dl
Requires:       mpv

%description
GNOME MPV interacts with mpv via the client API exported by libmpv, 
allowing access to mpv's powerful playback capabilities.

%prep
%setup -q

%build
autoreconf -sfi
intltoolize -c --automake
%configure
%make_build

%install
%make_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%changelog
* Mon Aug 17 2015 Maxim Orlov <murmansksity@gmai.com> - 0.5-1.R
- Initial package.
