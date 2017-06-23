# Copyright 2017 Adrien Vergé

Name:      some-nice-fonts
Version:   1.0.0
Release:   1%{?dist}
Summary:   Some nice fonts including Arial, Courier New, Helvetica, etc.
License:   Proprietary
URL:       https://github.com/adrienverge/copr-some-nice-fonts
Source0:   Arial.ttf
Source1:   ComicSansMs.ttf
Source2:   CourierNew.ttf
Source3:   Georgia.ttf
Source4:   HelveticaNeue.ttf
Source5:   Helvetica.ttf
Source6:   LucidaSansUnicode.ttf
Source7:   Tahoma.ttf
Source8:   TimesNewRoman.ttf
Source9:   TrebuchetMs.ttf
Source10:  Verdana.ttf

BuildArch: noarch
BuildRequires: fontpackages-devel

%description
This package provides the following fonts:
- Arial
- Comic Sans Ms
- Courier New
- Georgia
- Helvetica Neue
- Helvetica
- Lucida Sans Unicode
- Tahoma
- Times New Roman
- Trebuchet Ms
- Verdana


%_font_pkg -n some-nice-fonts *.ttf


%prep
%setup -q -c -T -n some-nice-fonts-%{version}


%build


%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontdir}


%files
%{_fontdir}/*.ttf


%changelog
* Fri Jun 23 2017 Adrien Vergé <adrienverge@gmail.com>
- Initial package spec
