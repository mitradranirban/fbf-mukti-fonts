# SPDX-License-Identifqier: MIT

Version:   3.0.1
	
Release:   2
	
URL:       https://github.com/mitradranirban/fbf-mukti-fonts
	
	
%global foundry fbf  
	
%global fontlicense       GPl3+ with exceptions
	
	
%global fontlicenses      LICENCE.txt
	
	
%global fontdocs          *.txt
	
%global fontdocsex        %{fontlicenses}
	
%global fontfamily        Mukti
	
%global fontsummary      Popular GPLed Bengali OpenType  font 
	
%global fonts            *.otf
	
%global fontconfs        %{_sourcedir}/fbf-mukti-fonts-3.0.1/67-font-mukti.conf
	
	
%global fontdescription  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font. It was made by using good quality glyphs of GPLed font bng2-n from Cyberscape Multimedia 
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>. It was made for Mukta Bangla Font project.
	
}
	
 %fontpkg  
	
%sourcelist
	
 %prep
	
%setup
	
	
%build
	
%fontbuild
	
	
%install
	
%fontinstall
	
	
%check
	
%fontcheck
	
	
%fontfiles
	
	
%changelog

* Wed Feb 02 2022 16:34:54 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-2
- Renamed spec  file as fonts-fbf-mukti - same as package name 
- corrected spec file errors  
* Fri Jan 28 2022 21:42:16 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1-1
- Change in EM square from 2048 to 1000
- Upgrade fto Unicode 14.0 standard for Bengali
- shift from version 1 to version 2 of Bengali OpenType specification
- support for Assamese language
- support for both traditional and modern form of conjunts 
- addition of vedic stress marks
- removal of Latin glyphs
- removal of references and over lapping 
- addition of missing conjuncts 
- various bugfixes 
- Removed Bengali namespace error of double utf-8 encoding
- Created Mukti from MuktiNarrow 
- Converted splines from quadratic to cubic
- saved source in fontforge sfd format 
- removed microsoft volt tables from font  
 
