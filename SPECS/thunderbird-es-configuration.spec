Name:		thunderbird-es-configuration
Version:	45.3.0
Release:	1%{?dist}
Summary:	Thunderbird configuration for Spanish user interface and dictionary

License:        GPLv3	
URL:		https://github.com/deskosproject/thunderbird-es-configuration

Requires:	hunspell-es
Requires:	thunderbird

%description
Thunderbird configuration for Spanish user interface and dictionary.

%install
mkdir -p %{buildroot}/usr/lib64/thunderbird/defaults/pref/
mkdir -p %{buildroot}/usr/lib64/thunderbird/extensions/

cat > %{buildroot}/usr/lib64/thunderbird/defaults/pref/spellchecker-dictionary-es.js <<EOF
pref("spellchecker.dictionary", "es");
EOF

ln -sf ../langpacks/langpack-es-ES@thunderbird.mozilla.org.xpi %{buildroot}/usr/lib64/thunderbird/extensions/

%files
%doc
/usr/lib64/thunderbird/defaults/pref/spellchecker-dictionary-es.js
/usr/lib64/thunderbird/extensions/langpack-es-ES@thunderbird.mozilla.org.xpi

%changelog
* Tue Sep 13 2016 Ricardo Arguello <rarguello@deskosproject.org> - 45.3.0-1
- Rebuilt for Thunderbird 45.3.0

* Wed Aug 10 2016 Ricardo Arguello <rarguello@deskosproject.org> - 45.2-1
- Rebuilt for Thunderbird 45.2
- Use a softlink to install the extension

* Tue May 17 2016 Ricardo Arguello <rarguello@deskosproject.org> - 38.8.0-1
- Initial release
