Name:		texlive-cabin
Version:	68373
Release:	1
Summary:	A humanist Sans Serif font, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cabin
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cabin is a humanist sans with four weights and true italics and
small capitals. According to the designer, Pablo Impallari,
Cabin was inspired by Edward Johnston's and Eric Gill's
typefaces, with a touch of modernism. Cabin incorporates modern
proportions, optical adjustments, and some elements of the
geometric sans. cabin.sty supports use of the font under LaTeX,
pdfLaTeX, xeLaTeX and luaLaTeX; it uses the mweights, to manage
the user's view of all those font weights. An sfdefault option
is provided to enable Cabin as the default text font. The
fontaxes package is required for use with [pdf]LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/cabin
%{_texmfdistdir}/fonts/map/dvips/cabin
%{_texmfdistdir}/fonts/opentype/impallari/cabin
%{_texmfdistdir}/fonts/tfm/impallari/cabin
%{_texmfdistdir}/fonts/type1/impallari/cabin
%{_texmfdistdir}/fonts/vf/impallari/cabin
%{_texmfdistdir}/tex/latex/cabin
%doc %{_texmfdistdir}/doc/fonts/cabin

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
