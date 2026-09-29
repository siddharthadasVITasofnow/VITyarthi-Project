# Design Diagrams

Written in Mermaid (GitHub shows them automatically). For the PDF report, paste each block into https://mermaid.live and export as an image, or redraw in draw.io.

## 1. System Architecture

```mermaid
flowchart TB
    User([User]) --> Main[main.py<br/>Menu]
    Main --> Encoder[encoder.py]
    Main --> Decoder[decoder.py]
    Main --> Signal[morse_signal.py]
    Main --> Logger[logger.py<br/>Session log]
    Encoder --> Validator[validator.py]
    Decoder --> Validator
    Signal --> Validator
    Encoder --> Map[(morse_map.py<br/>Dictionaries)]
    Decoder --> Map
    Validator --> Map
```

## 2. Workflow Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Show menu]
    B --> C{Choice}
    C -->|1| D[Enter text] --> E[encode]
    C -->|2| F[Enter Morse code] --> G[decode]
    C -->|3| H[Enter text] --> I[encode then show signal]
    C -->|4| J[Show session log]
    C -->|5| Z([Exit])
    C -->|Other| K[Show invalid choice]
    E --> L{Valid input?}
    G --> L
    I --> L
    L -->|Yes| M[Show result, log OK]
    L -->|No| N[Show error, log ERROR]
    M --> B
    N --> B
    J --> B
    K --> B
```

## 3. Use Case Diagram

```mermaid
flowchart LR
    U((User))
    subgraph System [Morse Code Converter]
        UC1([Convert text to Morse])
        UC2([Convert Morse to text])
        UC3([View signal pattern])
        UC4([View session log])
        UC5([Validate input])
    end
    U --- UC1
    U --- UC2
    U --- UC3
    U --- UC4
    UC1 -. include .-> UC5
    UC2 -. include .-> UC5
    UC3 -. include .-> UC5
```

## 4. Sequence Diagram (Text to Morse)

```mermaid
sequenceDiagram
    actor User
    participant M as main.py
    participant E as encoder.py
    participant V as validator.py
    participant D as morse_map.py
    participant L as logger.py
    User->>M: choose 1, type text
    M->>E: encode(text)
    E->>V: check_text(text)
    V->>D: check each character
    V-->>E: (True, "")
    E->>D: look up Morse for each character
    E-->>M: (True, morse)
    M-->>User: show Morse code
    M->>L: add_entry("ENCODE", "OK", text)
```

## 5. Component Diagram

The program uses functions in modules (no classes), so a component view is used.

```mermaid
classDiagram
    class morse_map {
        morse_code
        reverse_morse_code
        word_separator
    }
    class validator {
        find_unsupported()
        check_text()
        check_morse()
    }
    class encoder {
        encode()
    }
    class decoder {
        decode()
    }
    class morse_signal {
        build_units()
        draw_signal()
        total_duration()
        show_signal()
    }
    class logger {
        add_entry()
        show_log()
        count_status()
    }
    class main {
        show_menu()
        do_encode()
        do_decode()
        do_signal()
        main()
    }
    main --> encoder
    main --> decoder
    main --> morse_signal
    main --> logger
    encoder --> validator
    decoder --> validator
    morse_signal --> validator
    encoder --> morse_map
    decoder --> morse_map
    validator --> morse_map
```

## 6. ER Diagram

Not applicable: the project uses no database or file storage.
