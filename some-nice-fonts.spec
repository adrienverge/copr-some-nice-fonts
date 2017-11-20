# Copyright 2017 Adrien Vergé

Name:      some-nice-fonts
Version:   2.0.0
Release:   1%{?dist}
Summary:   Some nice fonts including Arial, Courier New, Helvetica, etc.
License:   Proprietary
URL:       https://github.com/adrienverge/copr-some-nice-fonts
Source0:   Arial.ttf
Source1:   ArialBd.ttf
Source2:   ArialIt.ttf
Source3:   ArialBdIt.ttf
Source4:   ComicSansMS.ttf
Source5:   ComicSansMSBd.ttf
Source6:   CourierNew.ttf
Source7:   Georgia.ttf
Source8:   GeorgiaBd.ttf
Source9:   GeorgiaIt.ttf
Source10:  GeorgiaBdIt.ttf
Source11:  Helvetica.ttf
Source12:  HelveticaBd.ttf
Source13:  HelveticaNeue.ttf
Source14:  HelveticaNeueBd.ttf
Source15:  LucidaSansUnicode.ttf
Source16:  Tahoma.ttf
Source17:  TahomaBd.ttf
Source18:  TimesNewRoman.ttf
Source19:  TimesNewRomanBd.ttf
Source20:  TimesNewRomanIt.ttf
Source21:  TimesNewRomanBdIt.ttf
Source22:  TrebuchetMS.ttf
Source23:  TrebuchetMSBd.ttf
Source24:  TrebuchetMSIt.ttf
Source25:  TrebuchetMSBdIt.ttf
Source26:  Verdana.ttf
Source27:  VerdanaBd.ttf
Source28:  VerdanaIt.ttf
Source29:  VerdanaBdIt.ttf

BuildArch: noarch
BuildRequires: fontpackages-devel

%description
This package provides the following fonts:
- Arial
- Comic Sans MS
- Courier New
- Georgia
- Helvetica Neue
- Helvetica
- Lucida Sans Unicode
- Tahoma
- Times New Roman
- Trebuchet MS
- Verdana


%_font_pkg -n some-nice-fonts *.ttf


%prep
%setup -q -c -T -n some-nice-fonts-%{version}


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
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE14} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE15} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE16} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE17} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE18} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE19} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE20} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE21} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE22} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE23} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE24} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE25} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE26} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE27} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE28} %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE29} %{buildroot}%{_fontdir}


%changelog
* Mon Nov 20 2017 Adrien Vergé <adrienverge@gmail.com>
- Add bold and italic versions when available

* Fri Jun 23 2017 Adrien Vergé <adrienverge@gmail.com>
- Initial package spec
