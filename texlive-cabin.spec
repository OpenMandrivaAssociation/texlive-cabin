%global tl_name cabin
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A humanist Sans Serif font, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cabin
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Cabin is a humanist sans with four weights and true italics and small
capitals. According to the designer, Pablo Impallari, Cabin was inspired
by Edward Johnston's and Eric Gill's typefaces, with a touch of
modernism. Cabin incorporates modern proportions, optical adjustments,
and some elements of the geometric sans. cabin.sty supports use of the
font under LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX; it uses the mweights,
to manage the user's view of all those font weights. An sfdefault option
is provided to enable Cabin as the default text font. The fontaxes
package is required for use with [pdf]LaTeX.

