# revision 31265
# category Package
# catalog-ctan /fonts/cabin
# catalog-date 2013-07-22 16:10:46 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-cabin
Version:	20130722
Release:	6
Summary:	A humanist Sans Serif font, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cabin
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cabin.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_6vzwvh.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_7kg2sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_aojlca.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_cgvdav.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_dh6h6g.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_eeshah.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_gi6ftn.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_gipwm5.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_hvmmj2.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_j5omty.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_jxvnp4.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_mzrldx.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_x3x2zv.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_xtln4x.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_xvjm53.enc
%{_texmfdistdir}/fonts/enc/dvips/cabin/cbn_zljgjy.enc
%{_texmfdistdir}/fonts/map/dvips/cabin/cabin.map
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-Medium.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-MediumItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-Regular.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-RegularItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-SemiBold.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/Cabin-SemiBoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-Medium.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-MediumItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-Regular.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-RegularItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-SemiBold.otf
%{_texmfdistdir}/fonts/opentype/impallari/cabin/CabinCondensed-SemiBoldItalic.otf
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/Cabin-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-MediumItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-RegularItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-Italic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-Medium.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-MediumItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-Regular.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-SemiBold.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/Cabin-SemiBoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-Medium.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-MediumItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-Regular.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-RegularItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-SemiBold.pfb
%{_texmfdistdir}/fonts/type1/impallari/cabin/CabinCondensed-SemiBoldItalic.pfb
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/Cabin-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-MediumItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-RegularItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/cabin/CabinCondensed-SemiBoldItalic-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/cabin/LY1Cabin-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/LY1CabinCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/OT1Cabin-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/OT1CabinCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/T1Cabin-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/T1CabinCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/TS1Cabin-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/TS1CabinCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/cabin/cabin.sty
%doc %{_texmfdistdir}/doc/fonts/cabin/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/cabin/README
%doc %{_texmfdistdir}/doc/fonts/cabin/samples-condensed.pdf
%doc %{_texmfdistdir}/doc/fonts/cabin/samples.pdf
%doc %{_texmfdistdir}/doc/fonts/cabin/samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
