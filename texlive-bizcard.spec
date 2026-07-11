%global tl_name bizcard
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset business cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bizcard
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bizcard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an adaption for current LaTeX of a LaTeX 2.09 style by Silvano
Balemi. It produces cards at the normal US card size, 76.2mm x 50.8mm.

