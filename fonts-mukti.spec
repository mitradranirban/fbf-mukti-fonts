# SPDX-License-Identifqier: MIT
	
%dnl Packaging template: basic single-family fonts packaging.
	
%dnl
	
%dnl This template documents the minimal set of spec declarations, necessary to
	
%dnl package a single font family, from a single dedicated source archive.
	
%dnl
	
%dnl It is part of the following set of packaging templates:
	
%dnl “fonts-0-simple”: basic single-family fonts packaging
	
%dnl “fonts-1-full”:   less common patterns for single-family fonts packaging
	
%dnl “fonts-2-multi”:  multi-family fonts packaging
	
%dnl “fonts-3-sub”:    packaging fonts, released as part of something else
	
%dnl
	
%dnl A font family is composed of font files, that share a single design, and
	
%dnl differ ONLY in:
	
%dnl — Weight        Bold, Black…
	
%dnl – Width∕Stretch Narrow, Condensed, Expanded…
	
%dnl — Slope/Slant   Italic, Oblique
	
%dnl Optical sizing  Caption…
	
%dnl
	
%dnl Those parameters correspond to the default axes of OpenType variable fonts:
	
%dnl https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags
	
%dnl The variable fonts model is an extension of the WWS model described in the
	
%dnl WPF Font Selection Model whitepaper (2007):
	
%dnl https://msdnshared.blob.core.windows.net/media/MSDNBlogsFS/prod.evol.blogs.msdn.com/CommunityServer.Components.PostAttachments/00/02/24/90/36/WPF%20Font%20Selection%20Model.pdf
	
%dnl
	
%dnl Do not rely on the naming upstream chose, to define family boundaries, it
	
%dnl will often be wrong.
	
%dnl
	
%dnl Declaration order is chosen to limit divergence between those templates, and
	
%dnl simplify cut and pasting.
	
%dnl
	
%global  fontfamily mukti
Version:   3.0.1
	
Release:   1
	
URL:       https://github.com/mitradranirban/fonts-mukti
	
 
	
%dnl The identifier of the entity, that released the font family.
	
 %global foundry fbf  
          
	
%dnl The font family license identifier. Adjust as necessary. The OFL is our
	
%dnl recommended font license.
	
%global fontlicense       GPl3+FontException
	
%dnl
	
%dnl The following directives are lists of space-separated shell globs
	
%dnl   – matching files associated with the font family,
	
%dnl   – as they exist in the build root,
	
%dnl   — at the end of the %build stage:
	
%dnl – legal files (licensing…)
	
%global fontlicenses      LICENCE.txt
	
%dnl – documentation files
	
%global fontdocs          *.txt
	
%dnl – exclusions from the ”fontdocs” list
	
%global fontdocsex        %{fontlicenses}
	
 
	
%dnl The human-friendly font family name, whitespace included, restricted to the
	
%dnl the Basic Latin Unicode block.
	
%global fontfamily0        Mukti
	
%global fontsummary0      Popular GPLed Bengali OpenType  font 
	
%dnl
	
%dnl More shell glob lists:
	
%dnl – font family files
	
%global fonts0            *.otf
	
%dnl – fontconfig files
	
%dnl   You can use %{SOURCEX}… instead of %{_sourcedir}/…, with X the number of
	
%dnl   the corresponding %sourcelist line.
	
%dnl   %sourcelist line numbering starts at 0.
	
%global fontconfs0        %{_sourcedir}/fbf-mukti-fonts-3.0.1/67-font-mukti.conf
	
%dnl A multi-line description block for the generated package.
	
%global fontdescription0  %{expand:
This is a one of the earliest Open Source OpenType Bengali / Bangla font It was made by using good quality glyphs of GPLed font bng2-n from Cyberscape Multimedia 
<https://web.archive.org/web/20021113130716/http://www.akruti.com/freedom/>. It was made for Mukta Bangla Font project.
	
}
	
 
	
%dnl Generate the font package headers corresponding to the elements declared
	
%dnl above.
	
%fontpkg fbf-mukti-fonts
	
%dnl Source declarations. Due to backwards-incompatible changes in rpm 4.15,
	
%dnl the %sourcelist/%patchlist style of source and patch declaration is a
	
%dnl requirement for safe font macro use.
	
%dnl Make sure to declare the main source archive before the other sources;
	
%dnl %setup processes %{SOURCE0} by default.
	
%sourcelist
	
 
	
%foundry-%fontfamily-fonts-%version.tar.gz
 	
 
	
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

* Fri Jan 28 2022 21:42:16 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  3.0.1
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
* Wed Sep 19 2018 20:02:43 +0530  Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.1.0
- added Open type tables to font
* Tue Nov 10 2015 07:16:51 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 2.0.0
- Removed Bengali namespace error of double utf-8 encoding
* Thu Jan 26 2006 +00:00:00 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> - 1.9.9
- Created Mukti from MuktiNarrow 
- Converted splines from quadratic to cubic
- saved source in fontforge sfd format 
- removed microsoft volt tables from font  
 


