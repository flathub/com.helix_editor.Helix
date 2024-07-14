# Flatpak for [the Helix editor](https://github.com/helix-editor/helix)

## To update:

- Clone the helix repo and checkout desired version
  ```sh
  git clone https://github.com/helix-editor/helix
  git -C helix switch --detach 24.07
  ```

- Use [flatpak-cargo-generator.py](https://github.com/flatpak/flatpak-builder-tools/tree/master/cargo)
  to generate `cargo-sources.json` from `helix/Cargo.lock`:
  ```sh
  python flatpak-cargo-generator.py helix/Cargo.lock -o cargo-sources.json
  ```

- Use `grammars/parse_languages.py` to generate `grammars/grammar-sources.json`
  from `helix/languages.toml`:
  ```sh
  python grammars/parse_languages.py ./helix/languages.toml
  ```

- Change url and checksum of helix source code in `com.helix_editor.Helix.yml`

- Build and locally install the flatpak:
  ```
  flatpak-builder build-dir com.helix_editor.Helix.yml --user --install --force-clean --ccache
  ```
