#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A81AF8E6ADBB200 (daenzer@debian.org)
#
Name     : xf86-video-ati
Version  : 18.0.1
Release  : 10
URL      : https://www.x.org/releases/individual/driver/xf86-video-ati-18.0.1.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-ati-18.0.1.tar.gz
Source99 : https://www.x.org/releases/individual/driver/xf86-video-ati-18.0.1.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-ati-lib
Requires: xf86-video-ati-data
Requires: xf86-video-ati-doc
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_radeon)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-ati - ATI/AMD Radeon video driver for the Xorg X server
Patches and questions regarding this software should be directed at the
amd-gfx mailing list:

%package data
Summary: data components for the xf86-video-ati package.
Group: Data

%description data
data components for the xf86-video-ati package.


%package doc
Summary: doc components for the xf86-video-ati package.
Group: Documentation

%description doc
doc components for the xf86-video-ati package.


%package lib
Summary: lib components for the xf86-video-ati package.
Group: Libraries
Requires: xf86-video-ati-data

%description lib
lib components for the xf86-video-ati package.


%prep
%setup -q -n xf86-video-ati-18.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522462068
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522462068
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-radeon.conf

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/ati_drv.so
/usr/lib64/xorg/modules/drivers/radeon_drv.so
