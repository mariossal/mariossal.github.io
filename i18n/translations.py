#!/usr/bin/env python3
"""Source of the translation tables. Run to regenerate i18n/el.json, it.json, es.json."""
import json, os
T = []
def t(en, el, it, es): T.append((en, el, it, es))

# Navigation
t('Home', 'Αρχική', 'Home', 'Inicio')
t('Research', 'Έρευνα', 'Ricerca', 'Investigación')
t('Projects', 'Έργα', 'Progetti', 'Proyectos')
t('Services', 'Υπηρεσίες', 'Servizi', 'Servicios')
t('Teaching', 'Διδασκαλία', 'Didattica', 'Docencia')
t('Electrical Engineering · Politecnico di Milano', 'Ηλεκτρολόγος Μηχανικός · Politecnico di Milano', 'Ingegneria Elettrica · Politecnico di Milano', 'Ingeniería Eléctrica · Politecnico di Milano')

# Home
t('Based in Milano, IT', 'Έδρα: Μιλάνο, Ιταλία', 'Con sede a Milano, IT', 'Con sede en Milán, IT')
t('Doctor of Philosophy in Electrical Engineering · Lecturer · AI Expert · Politecnico di Milano',
  'Διδάκτωρ Ηλεκτρολόγος Μηχανικός · Διδάσκων · Ειδικός Τεχνητής Νοημοσύνης · Politecnico di Milano',
  'Dottore di ricerca in Ingegneria Elettrica · Docente · Esperto di IA · Politecnico di Milano',
  'Doctor en Ingeniería Eléctrica · Docente · Experto en IA · Politecnico di Milano')
t('Electrical engineer working on forecasting, optimization and decision-focused learning for microgrids and battery energy storage.',
  'Ηλεκτρολόγος μηχανικός με αντικείμενο την πρόβλεψη, τη βελτιστοποίηση και τη μάθηση προσανατολισμένη στην απόφαση για μικροδίκτυα και συστήματα αποθήκευσης ενέργειας σε μπαταρίες.',
  'Ingegnere elettrico che si occupa di previsione, ottimizzazione e decision-focused learning per microreti e sistemi di accumulo a batteria.',
  'Ingeniero eléctrico dedicado a la predicción, la optimización y el aprendizaje orientado a la decisión para microrredes y almacenamiento en baterías.')
t('About', 'Σχετικά', 'Chi sono', 'Sobre mí')
t('In short', 'Εν συντομία', 'In breve', 'En pocas palabras')
t('I am a final-year PhD candidate in Electrical Engineering at Politecnico di Milano, in the Microgrids and Machine Learning Laboratory (MG²Lab). My thesis,',
  'Είμαι υποψήφιος διδάκτορας Ηλεκτρολόγος Μηχανικός στο τελευταίο έτος στο Politecnico di Milano, στο εργαστήριο Microgrids and Machine Learning (MG²Lab). Η διατριβή μου,',
  'Sono dottorando all\'ultimo anno in Ingegneria Elettrica al Politecnico di Milano, nel laboratorio Microgrids and Machine Learning (MG²Lab). La mia tesi,',
  'Soy doctorando de último año en Ingeniería Eléctrica en el Politecnico di Milano, en el laboratorio Microgrids and Machine Learning (MG²Lab). Mi tesis,')
t(', answers it with cost-aware loss functions, decision-focused learning trained through the dispatch optimizer, regret guarantees for the online case, game-theoretic coordination of forecasters, risk-averse training and a shadow-price diagnostic for forecast errors.',
  ', απαντά με συναρτήσεις κόστους ευαίσθητες στην τιμή, μάθηση προσανατολισμένη στην απόφαση που εκπαιδεύεται μέσα από τον βελτιστοποιητή κατανομής, εγγυήσεις regret για την online περίπτωση, συντονισμό πολλαπλών προβλεπτών με θεωρία παιγνίων, εκπαίδευση με αποστροφή κινδύνου και ένα διαγνωστικό σκιωδών τιμών για τα σφάλματα πρόβλεψης.',
  ', risponde con funzioni di perdita sensibili al costo, decision-focused learning addestrato attraverso l\'ottimizzatore di dispacciamento, garanzie di regret per il caso online, coordinamento game-theoretic dei previsori, addestramento avverso al rischio e una diagnostica basata sui prezzi ombra per gli errori di previsione.',
  ', responde con funciones de pérdida sensibles al coste, aprendizaje orientado a la decisión entrenado a través del optimizador de despacho, garantías de regret para el caso online, coordinación de predictores mediante teoría de juegos, entrenamiento averso al riesgo y un diagnóstico de precios sombra para los errores de predicción.')
t('Before Milan I studied Electrical and Computer Engineering at the University of Western Macedonia, with an Erasmus semester at Universidad Politécnica de Madrid. I have designed and commissioned photovoltaic plants in Greece, managed Horizon Europe projects on renewable energy, and led the forecasting division of DomOpti, a Politecnico di Milano spin-off. In 2025 and 2026 I spent a research semester at Polytechnique Montréal working on end-to-end learning for energy systems. At PoliMi I also teach master-level courses on circuits and electric energy conversion.',
  'Πριν από το Μιλάνο σπούδασα Ηλεκτρολόγος Μηχανικός και Μηχανικός Υπολογιστών στο Πανεπιστήμιο Δυτικής Μακεδονίας, με ένα εξάμηνο Erasmus στο Universidad Politécnica de Madrid. Έχω σχεδιάσει και θέσει σε λειτουργία φωτοβολταϊκούς σταθμούς στην Ελλάδα, έχω διαχειριστεί έργα Horizon Europe για τις ανανεώσιμες πηγές ενέργειας και έχω ηγηθεί του τμήματος προβλέψεων της DomOpti, spin-off του Politecnico di Milano. Το 2025 και το 2026 πέρασα ένα ερευνητικό εξάμηνο στο Polytechnique Montréal δουλεύοντας πάνω στη μάθηση end-to-end για ενεργειακά συστήματα. Στο PoliMi διδάσκω επίσης μεταπτυχιακά μαθήματα κυκλωμάτων και ηλεκτρικής μετατροπής ενέργειας.',
  'Prima di Milano ho studiato Ingegneria Elettrica e Informatica all\'Università della Macedonia Occidentale, con un semestre Erasmus alla Universidad Politécnica de Madrid. Ho progettato e messo in servizio impianti fotovoltaici in Grecia, gestito progetti Horizon Europe sulle energie rinnovabili e guidato la divisione previsioni di DomOpti, spin-off del Politecnico di Milano. Nel 2025 e 2026 ho trascorso un semestre di ricerca al Polytechnique Montréal lavorando sull\'apprendimento end-to-end per i sistemi energetici. Al PoliMi insegno inoltre corsi magistrali di circuiti e conversione elettrica dell\'energia.',
  'Antes de Milán estudié Ingeniería Eléctrica e Informática en la Universidad de Macedonia Occidental, con un semestre Erasmus en la Universidad Politécnica de Madrid. He diseñado y puesto en marcha plantas fotovoltaicas en Grecia, gestionado proyectos Horizon Europe sobre energías renovables y dirigido la división de predicción de DomOpti, una spin-off del Politecnico di Milano. En 2025 y 2026 realicé un semestre de investigación en Polytechnique Montréal trabajando en aprendizaje end-to-end para sistemas energéticos. En el PoliMi también imparto asignaturas de máster sobre circuitos y conversión eléctrica de la energía.')
t('Path', 'Διαδρομή', 'Percorso', 'Trayectoria')
t('2016 to today', '2016 έως σήμερα', 'Dal 2016 a oggi', 'De 2016 a hoy')
t('Diploma ECE', 'Δίπλωμα ΗΜΜΥ', 'Laurea ECE', 'Título ECE')
t('PV plants', 'Φ/Β σταθμοί', 'Impianti FV', 'Plantas FV')
t('EU Project Manager', 'Διαχειριστής έργων ΕΕ', 'Project Manager UE', 'Gestor de proyectos UE')
t('Greece', 'Ελλάδα', 'Grecia', 'Grecia')
t('PhD, MG²Lab', 'Διδακτορικό, MG²Lab', 'Dottorato, MG²Lab', 'Doctorado, MG²Lab')
t('Teaching Assistant', 'Βοηθός διδασκαλίας', 'Assistente alla didattica', 'Profesor asistente')
t('Visiting Researcher', 'Επισκέπτης ερευνητής', 'Ricercatore visitatore', 'Investigador visitante')
t('Diploma in Electrical and Computer Engineering, University of Western Macedonia',
  'Δίπλωμα Ηλεκτρολόγου Μηχανικού και Μηχανικού Υπολογιστών, Πανεπιστήμιο Δυτικής Μακεδονίας',
  'Laurea in Ingegneria Elettrica e Informatica, Università della Macedonia Occidentale',
  'Título en Ingeniería Eléctrica e Informática, Universidad de Macedonia Occidental')
t('Electrical Project Engineer, EcoEnergy SA', 'Ηλεκτρολόγος μηχανικός έργων, EcoEnergy SA', 'Ingegnere elettrico di progetto, EcoEnergy SA', 'Ingeniero eléctrico de proyectos, EcoEnergy SA')
t('Erasmus semester, Universidad Politécnica de Madrid', 'Εξάμηνο Erasmus, Universidad Politécnica de Madrid', 'Semestre Erasmus, Universidad Politécnica de Madrid', 'Semestre Erasmus, Universidad Politécnica de Madrid')
t('EU Project Manager, Cluster of Bioeconomy and Environment', 'Διαχειριστής έργων ΕΕ, Cluster Βιοοικονομίας και Περιβάλλοντος', 'Project Manager UE, Cluster of Bioeconomy and Environment', 'Gestor de proyectos UE, Cluster of Bioeconomy and Environment')
t('PhD, MG²Lab, Politecnico di Milano', 'Διδακτορικό, MG²Lab, Politecnico di Milano', 'Dottorato, MG²Lab, Politecnico di Milano', 'Doctorado, MG²Lab, Politecnico di Milano')
t('Teaching Assistant, Politecnico di Milano', 'Βοηθός διδασκαλίας, Politecnico di Milano', 'Assistente alla didattica, Politecnico di Milano', 'Profesor asistente, Politecnico di Milano')
t('Visiting Researcher, Polytechnique Montréal', 'Επισκέπτης ερευνητής, Polytechnique Montréal', 'Ricercatore visitatore, Polytechnique Montréal', 'Investigador visitante, Polytechnique Montréal')
t('If a forecast exists to drive a battery schedule, why train it to minimize squared error?',
  'Αν μια πρόβλεψη υπάρχει για να καθοδηγεί τον προγραμματισμό μιας μπαταρίας, γιατί να την εκπαιδεύουμε ώστε να ελαχιστοποιεί το τετραγωνικό σφάλμα;',
  'Se una previsione esiste per guidare la programmazione di una batteria, perché addestrarla a minimizzare l\'errore quadratico?',
  '¿Si una predicción existe para gobernar la programación de una batería, por qué entrenarla para minimizar el error cuadrático?')
t('Expertise', 'Εξειδίκευση', 'Competenze', 'Especialización')
t('What I work on', 'Με τι ασχολούμαι', 'Di cosa mi occupo', 'En qué trabajo')
t('Decision-focused learning', 'Μάθηση προσανατολισμένη στην απόφαση', 'Decision-focused learning', 'Aprendizaje orientado a la decisión')
t('Training forecasters through the optimization problem they feed, so that accuracy is measured in operating cost. Offline, online with regret guarantees, multi-forecaster and risk-averse variants.',
  'Εκπαίδευση προβλεπτών μέσα από το πρόβλημα βελτιστοποίησης που τροφοδοτούν, ώστε η ακρίβεια να μετριέται σε λειτουργικό κόστος. Παραλλαγές offline, online με εγγυήσεις regret, πολλαπλών προβλεπτών και με αποστροφή κινδύνου.',
  'Addestramento dei previsori attraverso il problema di ottimizzazione che alimentano, così che l\'accuratezza sia misurata in costo operativo. Varianti offline, online con garanzie di regret, multi-previsore e avverse al rischio.',
  'Entrenamiento de predictores a través del problema de optimización que alimentan, de modo que la precisión se mida en coste operativo. Variantes offline, online con garantías de regret, multipredictor y aversas al riesgo.')
t('Energy forecasting', 'Ενεργειακές προβλέψεις', 'Previsione energetica', 'Predicción energética')
t('Point and probabilistic forecasting of PV generation, load and electricity prices with gradient boosting, neural networks, conformal prediction and Gaussian processes.',
  'Σημειακές και πιθανοτικές προβλέψεις φωτοβολταϊκής παραγωγής, φορτίου και τιμών ηλεκτρικής ενέργειας με gradient boosting, νευρωνικά δίκτυα, conformal prediction και γκαουσιανές διεργασίες.',
  'Previsione puntuale e probabilistica di produzione fotovoltaica, carico e prezzi dell\'energia con gradient boosting, reti neurali, conformal prediction e processi gaussiani.',
  'Predicción puntual y probabilística de generación fotovoltaica, carga y precios de la electricidad con gradient boosting, redes neuronales, conformal prediction y procesos gaussianos.')
t('Microgrid optimization', 'Βελτιστοποίηση μικροδικτύων', 'Ottimizzazione di microreti', 'Optimización de microrredes')
t('Battery and EV-charging scheduling as LP and MILP problems, stochastic and reserve-constrained dispatch, sensitivity analysis through duality and multiparametric programming.',
  'Προγραμματισμός μπαταριών και φόρτισης ηλεκτρικών οχημάτων ως προβλήματα LP και MILP, στοχαστική κατανομή με περιορισμούς εφεδρείας, ανάλυση ευαισθησίας μέσω δυϊκότητας και πολυπαραμετρικού προγραμματισμού.',
  'Programmazione di batterie e ricarica di veicoli elettrici come problemi LP e MILP, dispacciamento stocastico e con vincoli di riserva, analisi di sensitività tramite dualità e programmazione multiparametrica.',
  'Programación de baterías y recarga de vehículos eléctricos como problemas LP y MILP, despacho estocástico y con restricciones de reserva, análisis de sensibilidad mediante dualidad y programación multiparamétrica.')
t('PV systems', 'Φωτοβολταϊκά συστήματα', 'Sistemi fotovoltaici', 'Sistemas fotovoltaicos')
t('Plant engineering background and data-driven monitoring of photovoltaic fleets, including peer-based probabilistic performance assessment.',
  'Υπόβαθρο μηχανικού φωτοβολταϊκών σταθμών και παρακολούθηση στόλων φωτοβολταϊκών με βάση τα δεδομένα, συμπεριλαμβανομένης πιθανοτικής αξιολόγησης απόδοσης σε σύγκριση με ομοειδείς σταθμούς.',
  'Esperienza di ingegneria degli impianti e monitoraggio data-driven di flotte fotovoltaiche, inclusa la valutazione probabilistica delle prestazioni rispetto a impianti simili.',
  'Experiencia en ingeniería de plantas y monitorización basada en datos de parques fotovoltaicos, incluida la evaluación probabilística del rendimiento frente a plantas comparables.')
t('Applied machine learning', 'Εφαρμοσμένη μηχανική μάθηση', 'Machine learning applicato', 'Aprendizaje automático aplicado')
t('Python, PyTorch, TensorFlow, XGBoost, CVXPY, Pyomo and Gurobi, with Docker, Grafana and time-series databases for deployed forecasting pipelines.',
  'Python, PyTorch, TensorFlow, XGBoost, CVXPY, Pyomo και Gurobi, με Docker, Grafana και βάσεις χρονοσειρών για παραγωγικές ροές πρόβλεψης.',
  'Python, PyTorch, TensorFlow, XGBoost, CVXPY, Pyomo e Gurobi, con Docker, Grafana e database di serie temporali per pipeline di previsione in produzione.',
  'Python, PyTorch, TensorFlow, XGBoost, CVXPY, Pyomo y Gurobi, con Docker, Grafana y bases de datos de series temporales para pipelines de predicción en producción.')
t('Research and project management', 'Έρευνα και διαχείριση έργων', 'Ricerca e gestione di progetti', 'Investigación y gestión de proyectos')
t('Horizon Europe projects MOST, MESSI and NEST, coordination of cross-national consortia, and validation on the MG²Lab microgrid testbed.',
  'Έργα Horizon Europe MOST, MESSI και NEST, συντονισμός διακρατικών κοινοπραξιών και επικύρωση στο πειραματικό μικροδίκτυο του MG²Lab.',
  'Progetti Horizon Europe MOST, MESSI e NEST, coordinamento di consorzi internazionali e validazione sul banco prova della microrete MG²Lab.',
  'Proyectos Horizon Europe MOST, MESSI y NEST, coordinación de consorcios internacionales y validación en el banco de pruebas de la microrred MG²Lab.')
t('Contact', 'Επικοινωνία', 'Contatti', 'Contacto')
t('Get in touch', 'Επικοινωνήστε μαζί μου', 'Scrivimi', 'Escríbeme')
t('Copy address', 'Αντιγραφή διεύθυνσης', 'Copia indirizzo', 'Copiar dirección')
t('Politecnico di Milano · Department of Energy · Via Lambruschini 4, 20156 Milano, Italy',
  'Politecnico di Milano · Τμήμα Ενέργειας · Via Lambruschini 4, 20156 Μιλάνο, Ιταλία',
  'Politecnico di Milano · Dipartimento di Energia · Via Lambruschini 4, 20156 Milano, Italia',
  'Politecnico di Milano · Departamento de Energía · Via Lambruschini 4, 20156 Milán, Italia')
t('Marios Saleptsis, PhD in Electrical Engineering at Politecnico di Milano. Forecasting, optimization and decision-focused learning for microgrids and battery energy storage.',
  'Μάριος Σαλέπτσης, Διδάκτωρ Ηλεκτρολόγος Μηχανικός στο Politecnico di Milano. Πρόβλεψη, βελτιστοποίηση και μάθηση προσανατολισμένη στην απόφαση για μικροδίκτυα και αποθήκευση ενέργειας σε μπαταρίες.',
  'Marios Saleptsis, dottore di ricerca in Ingegneria Elettrica al Politecnico di Milano. Previsione, ottimizzazione e decision-focused learning per microreti e accumulo a batteria.',
  'Marios Saleptsis, doctor en Ingeniería Eléctrica por el Politecnico di Milano. Predicción, optimización y aprendizaje orientado a la decisión para microrredes y almacenamiento en baterías.')

# Footer
t('Politecnico di Milano, Department of Energy', 'Politecnico di Milano, Τμήμα Ενέργειας', 'Politecnico di Milano, Dipartimento di Energia', 'Politecnico di Milano, Departamento de Energía')
t('Via Lambruschini 4, 20156 Milano, Italy', 'Via Lambruschini 4, 20156 Μιλάνο, Ιταλία', 'Via Lambruschini 4, 20156 Milano, Italia', 'Via Lambruschini 4, 20156 Milán, Italia')
t('Links', 'Σύνδεσμοι', 'Collegamenti', 'Enlaces')
t('CV (PDF)', 'Βιογραφικό (PDF)', 'CV (PDF)', 'CV (PDF)')
t('Colophon', 'Κολοφώνας', 'Colophon', 'Colofón')
t('Milan · MG²Lab · Politecnico di Milano', 'Μιλάνο · MG²Lab · Politecnico di Milano', 'Milano · MG²Lab · Politecnico di Milano', 'Milán · MG²Lab · Politecnico di Milano')
t('Last updated September 2026', 'Τελευταία ενημέρωση Σεπτέμβριος 2026', 'Ultimo aggiornamento settembre 2026', 'Última actualización septiembre de 2026')

# Research
t('Research · Marios Saleptsis', 'Έρευνα · Marios Saleptsis', 'Ricerca · Marios Saleptsis', 'Investigación · Marios Saleptsis')
t('Forecasts judged by the decisions they cause', 'Προβλέψεις που κρίνονται από τις αποφάσεις που προκαλούν', 'Previsioni giudicate dalle decisioni che provocano', 'Predicciones juzgadas por las decisiones que provocan')
t('A microgrid energy management system forecasts load, PV and prices, then solves a dispatch problem. My work closes that loop: the forecaster is trained on the cost of the schedule it produces, and the theory says when that is guaranteed to help.',
  'Ένα σύστημα διαχείρισης ενέργειας μικροδικτύου προβλέπει φορτίο, φωτοβολταϊκή παραγωγή και τιμές και έπειτα λύνει ένα πρόβλημα κατανομής. Η δουλειά μου κλείνει αυτόν τον βρόχο: ο προβλέπτης εκπαιδεύεται στο κόστος του προγράμματος που παράγει, και η θεωρία λέει πότε αυτό βοηθά με εγγύηση.',
  'Un sistema di gestione dell\'energia di una microrete prevede carico, fotovoltaico e prezzi, poi risolve un problema di dispacciamento. Il mio lavoro chiude quell\'anello: il previsore è addestrato sul costo del programma che produce, e la teoria dice quando ciò è garantito essere utile.',
  'Un sistema de gestión de energía de una microrred predice carga, fotovoltaica y precios y después resuelve un problema de despacho. Mi trabajo cierra ese bucle: el predictor se entrena sobre el coste del programa que produce, y la teoría dice cuándo eso ayuda con garantía.')
t('Summary', 'Σύνοψη', 'Sintesi', 'Resumen')
t('The thesis in one page', 'Η διατριβή σε μία σελίδα', 'La tesi in una pagina', 'La tesis en una página')
t('Battery scheduling in a microgrid depends on forecasts of PV generation, load and electricity prices. The standard practice trains those forecasters for statistical accuracy and hands the result to an optimizer. My doctoral work replaces that separation with cost-aware and decision-focused training, where the forecaster is shaped by the operating cost of the dispatch it induces.',
  'Ο προγραμματισμός μπαταριών σε ένα μικροδίκτυο εξαρτάται από προβλέψεις φωτοβολταϊκής παραγωγής, φορτίου και τιμών ηλεκτρικής ενέργειας. Η καθιερωμένη πρακτική εκπαιδεύει αυτούς τους προβλέπτες για στατιστική ακρίβεια και παραδίδει το αποτέλεσμα σε έναν βελτιστοποιητή. Η διδακτορική μου έρευνα αντικαθιστά αυτόν τον διαχωρισμό με εκπαίδευση ευαίσθητη στο κόστος και προσανατολισμένη στην απόφαση, όπου ο προβλέπτης διαμορφώνεται από το λειτουργικό κόστος της κατανομής που προκαλεί.',
  'La programmazione delle batterie in una microrete dipende da previsioni di produzione fotovoltaica, carico e prezzi dell\'energia. La prassi standard addestra quei previsori per l\'accuratezza statistica e consegna il risultato a un ottimizzatore. Il mio lavoro di dottorato sostituisce quella separazione con un addestramento sensibile al costo e orientato alla decisione, in cui il previsore è modellato dal costo operativo del dispacciamento che induce.',
  'La programación de baterías en una microrred depende de predicciones de generación fotovoltaica, carga y precios de la electricidad. La práctica habitual entrena esos predictores para la precisión estadística y entrega el resultado a un optimizador. Mi trabajo doctoral sustituye esa separación por un entrenamiento sensible al coste y orientado a la decisión, en el que el predictor queda moldeado por el coste operativo del despacho que induce.')
t('The contributions run from practical to theoretical. Cost-aware loss functions and forecast selectors make an off-the-shelf PV forecaster price-sensitive without touching the optimizer. Decision-focused learning trains load and PV forecasters end to end through the BESS dispatch problem, and shows that forecasters with higher RMSE can produce lower cost, with reductions of',
  'Οι συνεισφορές εκτείνονται από το πρακτικό έως το θεωρητικό. Συναρτήσεις κόστους ευαίσθητες στην τιμή και επιλογείς προβλέψεων κάνουν έναν έτοιμο προβλέπτη φωτοβολταϊκών ευαίσθητο στις τιμές χωρίς να αγγίζουν τον βελτιστοποιητή. Η μάθηση προσανατολισμένη στην απόφαση εκπαιδεύει προβλέπτες φορτίου και φωτοβολταϊκών end-to-end μέσα από το πρόβλημα κατανομής του συστήματος μπαταριών και δείχνει ότι προβλέπτες με υψηλότερο RMSE μπορούν να δώσουν χαμηλότερο κόστος, με μειώσεις',
  'I contributi vanno dal pratico al teorico. Funzioni di perdita sensibili al costo e selettori di previsione rendono un previsore fotovoltaico standard sensibile ai prezzi senza toccare l\'ottimizzatore. Il decision-focused learning addestra previsori di carico e fotovoltaico end-to-end attraverso il problema di dispacciamento del BESS e mostra che previsori con RMSE più alto possono produrre costi più bassi, con riduzioni del',
  'Las contribuciones van de lo práctico a lo teórico. Las funciones de pérdida sensibles al coste y los selectores de predicción hacen que un predictor fotovoltaico estándar sea sensible a los precios sin tocar el optimizador. El aprendizaje orientado a la decisión entrena predictores de carga y fotovoltaica end-to-end a través del problema de despacho del BESS y muestra que predictores con mayor RMSE pueden producir menor coste, con reducciones del')
t('in normal operation and', 'σε κανονική λειτουργία και', 'in funzionamento normale e del', 'en operación normal y del')
t('when grid exchange is constrained. For online training, I prove the first regret guarantees through a dispatch optimizer whose state of charge carries every past mistake forward. When several forecasters are trained separately, a potential-game formulation with a Stackelberg-Nash scheme coordinates them. Risk-averse training applies Conditional Value-at-Risk to the regret distribution so the tail of bad scheduling days shapes the model. Finally, a shadow-price diagnostic gives an exact, certified attribution of cost to individual forecast errors, explained by proximity to binding constraints, timing against the tariff, and direction of the error.',
  'όταν η ανταλλαγή με το δίκτυο είναι περιορισμένη. Για την online εκπαίδευση, αποδεικνύω τις πρώτες εγγυήσεις regret μέσα από έναν βελτιστοποιητή κατανομής του οποίου η κατάσταση φόρτισης μεταφέρει κάθε προηγούμενο λάθος στο μέλλον. Όταν πολλοί προβλέπτες εκπαιδεύονται χωριστά, μια διατύπωση δυναμικού παιγνίου με σχήμα Stackelberg-Nash τους συντονίζει. Η εκπαίδευση με αποστροφή κινδύνου εφαρμόζει Conditional Value-at-Risk στην κατανομή του regret, ώστε η ουρά των κακών ημερών προγραμματισμού να διαμορφώνει το μοντέλο. Τέλος, ένα διαγνωστικό σκιωδών τιμών δίνει μια ακριβή, πιστοποιημένη απόδοση του κόστους σε μεμονωμένα σφάλματα πρόβλεψης, που εξηγείται από την εγγύτητα σε ενεργούς περιορισμούς, τον χρονισμό ως προς το τιμολόγιο και την κατεύθυνση του σφάλματος.',
  'quando lo scambio con la rete è vincolato. Per l\'addestramento online dimostro le prime garanzie di regret attraverso un ottimizzatore di dispacciamento il cui stato di carica trasporta ogni errore passato nel futuro. Quando più previsori vengono addestrati separatamente, una formulazione a gioco potenziale con schema Stackelberg-Nash li coordina. L\'addestramento avverso al rischio applica il Conditional Value-at-Risk alla distribuzione del regret, così che la coda dei giorni di programmazione peggiori modelli il previsore. Infine, una diagnostica basata sui prezzi ombra fornisce un\'attribuzione esatta e certificata del costo ai singoli errori di previsione, spiegata dalla vicinanza ai vincoli attivi, dal tempismo rispetto alla tariffa e dalla direzione dell\'errore.',
  'cuando el intercambio con la red está restringido. Para el entrenamiento online, demuestro las primeras garantías de regret a través de un optimizador de despacho cuyo estado de carga arrastra cada error pasado hacia el futuro. Cuando varios predictores se entrenan por separado, una formulación de juego potencial con un esquema Stackelberg-Nash los coordina. El entrenamiento averso al riesgo aplica el Conditional Value-at-Risk a la distribución del regret, de modo que la cola de los peores días de programación moldea el modelo. Por último, un diagnóstico de precios sombra ofrece una atribución exacta y certificada del coste a errores de predicción individuales, explicada por la proximidad a restricciones activas, el momento respecto a la tarifa y la dirección del error.')
t('All of it is validated on the MG²Lab microgrid at Politecnico di Milano, with up to', 'Όλα επικυρώνονται στο μικροδίκτυο του MG²Lab στο Politecnico di Milano, με έως', 'Tutto è validato sulla microrete MG²Lab del Politecnico di Milano, con fino a', 'Todo ello se valida en la microrred MG²Lab del Politecnico di Milano, con hasta')
t('of PV, a', 'φωτοβολταϊκών, ένα υβριδικό σύστημα αποθήκευσης', 'di fotovoltaico, un sistema di accumulo ibrido da', 'de fotovoltaica, un sistema de almacenamiento híbrido de')
t('hybrid storage system, a', ', μια μονάδα micro-CHP', ', un\'unità micro-CHP da', ', una unidad micro-CHP de')
t('micro-CHP unit, EV chargers and programmable loads, and within the Horizon Europe projects MOST, MESSI and NEST.',
  ', φορτιστές ηλεκτρικών οχημάτων και προγραμματιζόμενα φορτία, και στο πλαίσιο των έργων Horizon Europe MOST, MESSI και NEST.',
  ', colonnine per veicoli elettrici e carichi programmabili, e all\'interno dei progetti Horizon Europe MOST, MESSI e NEST.',
  ', cargadores de vehículos eléctricos y cargas programables, y en el marco de los proyectos Horizon Europe MOST, MESSI y NEST.')
t('Institutions', 'Ιδρύματα', 'Istituzioni', 'Instituciones')
t('Where the work was done', 'Πού έγινε η δουλειά', 'Dove è stato svolto il lavoro', 'Dónde se hizo el trabajo')
t('Doctoral research, teaching, MG²Lab', 'Διδακτορική έρευνα, διδασκαλία, MG²Lab', 'Ricerca di dottorato, didattica, MG²Lab', 'Investigación doctoral, docencia, MG²Lab')
t('Milan, Italy', 'Μιλάνο, Ιταλία', 'Milano, Italia', 'Milán, Italia')
t('Visiting researcher', 'Επισκέπτης ερευνητής', 'Ricercatore visitatore', 'Investigador visitante')
t('Montréal, Canada', 'Μόντρεαλ, Καναδάς', 'Montréal, Canada', 'Montreal, Canadá')
t('Erasmus semester, IoT and renewable energy laboratories', 'Εξάμηνο Erasmus, εργαστήρια IoT και ανανεώσιμων πηγών ενέργειας', 'Semestre Erasmus, laboratori IoT ed energie rinnovabili', 'Semestre Erasmus, laboratorios de IoT y energías renovables')
t('Madrid, Spain', 'Μαδρίτη, Ισπανία', 'Madrid, Spagna', 'Madrid, España')
t('University of Western Macedonia', 'Πανεπιστήμιο Δυτικής Μακεδονίας', 'Università della Macedonia Occidentale', 'Universidad de Macedonia Occidental')
t('Diploma in Electrical and Computer Engineering', 'Δίπλωμα Ηλεκτρολόγου Μηχανικού και Μηχανικού Υπολογιστών', 'Laurea in Ingegneria Elettrica e Informatica', 'Título en Ingeniería Eléctrica e Informática')
t('Kozani, Greece', 'Κοζάνη, Ελλάδα', 'Kozani, Grecia', 'Kozani, Grecia')
t('Methods', 'Μέθοδοι', 'Metodi', 'Métodos')
t('End-to-end training through LP and MILP dispatch', 'Εκπαίδευση end-to-end μέσα από κατανομή LP και MILP', 'Addestramento end-to-end attraverso dispacciamento LP e MILP', 'Entrenamiento end-to-end a través de despacho LP y MILP')
t('Online learning and regret analysis', 'Online μάθηση και ανάλυση regret', 'Apprendimento online e analisi del regret', 'Aprendizaje online y análisis de regret')
t('Game-theoretic multi-forecaster coordination', 'Συντονισμός πολλαπλών προβλεπτών με θεωρία παιγνίων', 'Coordinamento game-theoretic di più previsori', 'Coordinación de varios predictores mediante teoría de juegos')
t('Risk-averse (CVaR) training objectives', 'Στόχοι εκπαίδευσης με αποστροφή κινδύνου (CVaR)', 'Obiettivi di addestramento avversi al rischio (CVaR)', 'Objetivos de entrenamiento aversos al riesgo (CVaR)')
t('Zeroth-order methods for mixed-integer problems', 'Μέθοδοι μηδενικής τάξης για προβλήματα μικτών ακεραίων', 'Metodi di ordine zero per problemi misto-interi', 'Métodos de orden cero para problemas mixtos enteros')
t('Forecasting', 'Πρόβλεψη', 'Previsione', 'Predicción')
t('Cost-aware and asymmetric loss functions', 'Συναρτήσεις κόστους ευαίσθητες στην τιμή και ασύμμετρες', 'Funzioni di perdita sensibili al costo e asimmetriche', 'Funciones de pérdida sensibles al coste y asimétricas')
t('Gradient boosting and neural networks', 'Gradient boosting και νευρωνικά δίκτυα', 'Gradient boosting e reti neurali', 'Gradient boosting y redes neuronales')
t('Probabilistic forecasting: NGBoost, conformal prediction, sparse GP', 'Πιθανοτική πρόβλεψη: NGBoost, conformal prediction, αραιές GP', 'Previsione probabilistica: NGBoost, conformal prediction, GP sparsi', 'Predicción probabilística: NGBoost, conformal prediction, GP dispersos')
t('Forecast selection and combination', 'Επιλογή και συνδυασμός προβλέψεων', 'Selezione e combinazione di previsioni', 'Selección y combinación de predicciones')
t('Optimization and analysis', 'Βελτιστοποίηση και ανάλυση', 'Ottimizzazione e analisi', 'Optimización y análisis')
t('Battery and EV-charging scheduling', 'Προγραμματισμός μπαταριών και φόρτισης ηλεκτρικών οχημάτων', 'Programmazione di batterie e ricarica di veicoli elettrici', 'Programación de baterías y recarga de vehículos eléctricos')
t('Stochastic and reserve-constrained dispatch', 'Στοχαστική κατανομή με περιορισμούς εφεδρείας', 'Dispacciamento stocastico e con vincoli di riserva', 'Despacho estocástico y con restricciones de reserva')
t('Duality, envelope theorem and multiparametric sensitivity', 'Δυϊκότητα, θεώρημα περιβάλλουσας και πολυπαραμετρική ευαισθησία', 'Dualità, teorema dell\'inviluppo e sensitività multiparametrica', 'Dualidad, teorema de la envolvente y sensibilidad multiparamétrica')
t('Shadow-price diagnostics', 'Διαγνωστικά σκιωδών τιμών', 'Diagnostica a prezzi ombra', 'Diagnóstico de precios sombra')
t('Domains', 'Πεδία', 'Ambiti', 'Ámbitos')
t('Application areas', 'Πεδία εφαρμογής', 'Aree di applicazione', 'Áreas de aplicación')
t('Microgrids', 'Μικροδίκτυα', 'Microreti', 'Microrredes')
t('Battery energy storage', 'Αποθήκευση ενέργειας σε μπαταρίες', 'Accumulo a batteria', 'Almacenamiento en baterías')
t('Photovoltaic generation', 'Φωτοβολταϊκή παραγωγή', 'Produzione fotovoltaica', 'Generación fotovoltaica')
t('EV charging', 'Φόρτιση ηλεκτρικών οχημάτων', 'Ricarica di veicoli elettrici', 'Recarga de vehículos eléctricos')
t('Energy management systems', 'Συστήματα διαχείρισης ενέργειας', 'Sistemi di gestione dell\'energia', 'Sistemas de gestión de energía')
t('Electricity markets and tariffs', 'Αγορές ηλεκτρικής ενέργειας και τιμολόγια', 'Mercati elettrici e tariffe', 'Mercados eléctricos y tarifas')
t('PV fleet monitoring', 'Παρακολούθηση στόλων φωτοβολταϊκών', 'Monitoraggio di flotte fotovoltaiche', 'Monitorización de parques fotovoltaicos')
t('Hybrid storage', 'Υβριδική αποθήκευση', 'Accumulo ibrido', 'Almacenamiento híbrido')
t('Laboratory validation', 'Εργαστηριακή επικύρωση', 'Validazione in laboratorio', 'Validación en laboratorio')
t('Publications', 'Δημοσιεύσεις', 'Pubblicazioni', 'Publicaciones')
t('Under review and accepted', 'Υπό κρίση και αποδεκτές', 'In revisione e accettate', 'En revisión y aceptadas')
t('Full record on', 'Πλήρης κατάλογος στο', 'Elenco completo su', 'Registro completo en')
t('and', 'και', 'e', 'y')
t('Under review', 'Υπό κρίση', 'In revisione', 'En revisión')
t('Applied Energy, special issue Microgrids 2027', 'Applied Energy, ειδικό τεύχος Microgrids 2027', 'Applied Energy, numero speciale Microgrids 2027', 'Applied Energy, número especial Microgrids 2027')
t('Accepted', 'Αποδεκτή', 'Accettato', 'Aceptado')
t('ELECTRIMACS 2026, Palermo, Italy, May 2026', 'ELECTRIMACS 2026, Παλέρμο, Ιταλία, Μάιος 2026', 'ELECTRIMACS 2026, Palermo, Italia, maggio 2026', 'ELECTRIMACS 2026, Palermo, Italia, mayo de 2026')
t('Published', 'Δημοσιευμένες', 'Pubblicate', 'Publicadas')
t('Conference paper, July 2025', 'Άρθρο συνεδρίου, Ιούλιος 2025', 'Articolo di conferenza, luglio 2025', 'Artículo de congreso, julio de 2025')
t('Conference paper, June 2025', 'Άρθρο συνεδρίου, Ιούνιος 2025', 'Articolo di conferenza, giugno 2025', 'Artículo de congreso, junio de 2025')
t('Conference paper, October 2024', 'Άρθρο συνεδρίου, Οκτώβριος 2024', 'Articolo di conferenza, ottobre 2024', 'Artículo de congreso, octubre de 2024')
t('Conference paper, June 2024', 'Άρθρο συνεδρίου, Ιούνιος 2024', 'Articolo di conferenza, giugno 2024', 'Artículo de congreso, junio de 2024')
t('Forecasting, vol. 6, no. 3, 2024', 'Forecasting, τόμ. 6, αρ. 3, 2024', 'Forecasting, vol. 6, n. 3, 2024', 'Forecasting, vol. 6, n.º 3, 2024')
t('Journal', 'Περιοδικό', 'Rivista', 'Revista')
t('Thesis', 'Διατριβή', 'Tesi', 'Tesis')
t('Doctoral thesis', 'Διδακτορική διατριβή', 'Tesi di dottorato', 'Tesis doctoral')
t('· Supervisors: S. Leva, M. Mussetta', '· Επιβλέποντες: S. Leva, M. Mussetta', '· Relatori: S. Leva, M. Mussetta', '· Directores: S. Leva, M. Mussetta')
t('Politecnico di Milano, XXXIX cycle', 'Politecnico di Milano, 39ος κύκλος', 'Politecnico di Milano, XXXIX ciclo', 'Politecnico di Milano, ciclo XXXIX')
t('Defense expected November 2026', 'Υποστήριξη αναμένεται Νοέμβριο 2026', 'Discussione prevista a novembre 2026', 'Defensa prevista en noviembre de 2026')
t('Research summary, methods and publications of Marios Saleptsis: decision-focused forecasting for battery scheduling in microgrids.',
  'Σύνοψη έρευνας, μέθοδοι και δημοσιεύσεις του Μάριου Σαλέπτση: πρόβλεψη προσανατολισμένη στην απόφαση για τον προγραμματισμό μπαταριών σε μικροδίκτυα.',
  'Sintesi della ricerca, metodi e pubblicazioni di Marios Saleptsis: previsione orientata alla decisione per la programmazione di batterie in microreti.',
  'Resumen de investigación, métodos y publicaciones de Marios Saleptsis: predicción orientada a la decisión para la programación de baterías en microrredes.')
t('Politecnico di Milano logo', 'Λογότυπο Politecnico di Milano', 'Logo Politecnico di Milano', 'Logotipo del Politecnico di Milano')
t('Polytechnique Montréal logo', 'Λογότυπο Polytechnique Montréal', 'Logo Polytechnique Montréal', 'Logotipo de Polytechnique Montréal')
t('Universidad Politécnica de Madrid logo', 'Λογότυπο Universidad Politécnica de Madrid', 'Logo Universidad Politécnica de Madrid', 'Logotipo de la Universidad Politécnica de Madrid')
t('University of Western Macedonia logo', 'Λογότυπο Πανεπιστημίου Δυτικής Μακεδονίας', 'Logo Università della Macedonia Occidentale', 'Logotipo de la Universidad de Macedonia Occidental')

# Projects
t('Projects · Marios Saleptsis', 'Έργα · Marios Saleptsis', 'Progetti · Marios Saleptsis', 'Proyectos · Marios Saleptsis')
t('Research projects, software and applied work. This page is being written; entries will appear here as they are ready.',
  'Ερευνητικά έργα, λογισμικό και εφαρμοσμένη δουλειά. Η σελίδα γράφεται· οι καταχωρίσεις θα εμφανίζονται εδώ όταν είναι έτοιμες.',
  'Progetti di ricerca, software e lavoro applicato. Questa pagina è in scrittura; le voci compariranno qui man mano che saranno pronte.',
  'Proyectos de investigación, software y trabajo aplicado. Esta página está en preparación; las entradas aparecerán aquí a medida que estén listas.')
t('Coming soon', 'Σύντομα', 'Prossimamente', 'Próximamente')
t('In preparation', 'Σε προετοιμασία', 'In preparazione', 'En preparación')
t('Each project will have a short description, the role played, the tools used and, where possible, a link to code or results.',
  'Κάθε έργο θα έχει σύντομη περιγραφή, τον ρόλο μου, τα εργαλεία που χρησιμοποιήθηκαν και, όπου είναι δυνατόν, σύνδεσμο σε κώδικα ή αποτελέσματα.',
  'Ogni progetto avrà una breve descrizione, il ruolo svolto, gli strumenti usati e, dove possibile, un collegamento a codice o risultati.',
  'Cada proyecto tendrá una breve descripción, el papel desempeñado, las herramientas utilizadas y, cuando sea posible, un enlace al código o a los resultados.')
t('Placeholder. Send me a list of projects (name, one-line description, your role, links) and I will lay them out here in the same style as the rest of the site.',
  'Προσωρινό περιεχόμενο. Τα έργα θα προστεθούν σύντομα.',
  'Contenuto provvisorio. I progetti saranno aggiunti a breve.',
  'Contenido provisional. Los proyectos se añadirán en breve.')
t('Projects by Marios Saleptsis.', 'Έργα του Μάριου Σαλέπτση.', 'Progetti di Marios Saleptsis.', 'Proyectos de Marios Saleptsis.')

# Services
t('Services · Marios Saleptsis', 'Υπηρεσίες · Marios Saleptsis', 'Servizi · Marios Saleptsis', 'Servicios · Marios Saleptsis')
t('What I can do for you', 'Τι μπορώ να κάνω για εσάς', 'Cosa posso fare per voi', 'Qué puedo hacer por usted')
t('Consulting and technical work for utilities, developers, energy communities and companies building products around forecasting, batteries and photovoltaics. Scoped as a short study, a delivered model, or ongoing advisory.',
  'Συμβουλευτική και τεχνική εργασία για εταιρείες ηλεκτρισμού, developers, ενεργειακές κοινότητες και εταιρείες που χτίζουν προϊόντα γύρω από την πρόβλεψη, τις μπαταρίες και τα φωτοβολταϊκά. Ως σύντομη μελέτη, παραδοτέο μοντέλο ή συνεχής συμβουλευτική.',
  'Consulenza e lavoro tecnico per utility, sviluppatori, comunità energetiche e aziende che costruiscono prodotti intorno a previsione, batterie e fotovoltaico. Come studio breve, modello consegnato o consulenza continuativa.',
  'Consultoría y trabajo técnico para eléctricas, promotores, comunidades energéticas y empresas que construyen productos en torno a la predicción, las baterías y la fotovoltaica. Como estudio breve, modelo entregado o asesoría continuada.')
t('CV as PDF', 'Βιογραφικό σε PDF', 'CV in PDF', 'CV en PDF')
t('Offer', 'Προσφορά', 'Offerta', 'Oferta')
t('Day-ahead and intraday forecasts of PV generation, load and electricity prices, point or probabilistic, built on your data and delivered as a model you can run. Includes accuracy benchmarking against what you use today.',
  'Προβλέψεις day-ahead και intraday φωτοβολταϊκής παραγωγής, φορτίου και τιμών ηλεκτρικής ενέργειας, σημειακές ή πιθανοτικές, χτισμένες στα δεδομένα σας και παραδοτέες ως μοντέλο που μπορείτε να τρέξετε. Περιλαμβάνει σύγκριση ακρίβειας με ό,τι χρησιμοποιείτε σήμερα.',
  'Previsioni day-ahead e intraday di produzione fotovoltaica, carico e prezzi dell\'energia, puntuali o probabilistiche, costruite sui vostri dati e consegnate come modello eseguibile. Include il confronto di accuratezza con quanto usate oggi.',
  'Predicciones day-ahead e intradiarias de generación fotovoltaica, carga y precios de la electricidad, puntuales o probabilísticas, construidas sobre sus datos y entregadas como un modelo que puede ejecutar. Incluye la comparación de precisión con lo que usa hoy.')
t('Battery scheduling and EMS optimization', 'Προγραμματισμός μπαταριών και βελτιστοποίηση EMS', 'Programmazione di batterie e ottimizzazione EMS', 'Programación de baterías y optimización de EMS')
t('Dispatch strategies for battery storage, EV charging and microgrids under tariffs, grid limits and reserve requirements. LP and MILP formulations, from a feasibility study to a deployed scheduler.',
  'Στρατηγικές κατανομής για αποθήκευση σε μπαταρίες, φόρτιση ηλεκτρικών οχημάτων και μικροδίκτυα υπό τιμολόγια, όρια δικτύου και απαιτήσεις εφεδρείας. Διατυπώσεις LP και MILP, από μελέτη σκοπιμότητας έως εγκατεστημένο σύστημα προγραμματισμού.',
  'Strategie di dispacciamento per accumulo a batteria, ricarica di veicoli elettrici e microreti sotto tariffe, limiti di rete e requisiti di riserva. Formulazioni LP e MILP, dallo studio di fattibilità allo scheduler in produzione.',
  'Estrategias de despacho para almacenamiento en baterías, recarga de vehículos eléctricos y microrredes bajo tarifas, límites de red y requisitos de reserva. Formulaciones LP y MILP, desde el estudio de viabilidad hasta el programador en producción.')
t('Decision-focused forecasting', 'Πρόβλεψη προσανατολισμένη στην απόφαση', 'Previsione orientata alla decisione', 'Predicción orientada a la decisión')
t('Forecasters trained on the operating cost of the decisions they drive rather than on error metrics alone. The method behind my doctoral work, applied to your storage or trading problem.',
  'Προβλέπτες εκπαιδευμένοι στο λειτουργικό κόστος των αποφάσεων που καθοδηγούν και όχι μόνο σε μετρικές σφάλματος. Η μέθοδος πίσω από τη διδακτορική μου έρευνα, εφαρμοσμένη στο δικό σας πρόβλημα αποθήκευσης ή εμπορίας ενέργειας.',
  'Previsori addestrati sul costo operativo delle decisioni che guidano invece che sulle sole metriche di errore. Il metodo alla base del mio dottorato, applicato al vostro problema di accumulo o trading.',
  'Predictores entrenados sobre el coste operativo de las decisiones que gobiernan y no solo sobre métricas de error. El método de mi trabajo doctoral, aplicado a su problema de almacenamiento o trading.')
t('PV plant assessment and monitoring', 'Αξιολόγηση και παρακολούθηση φωτοβολταϊκών σταθμών', 'Valutazione e monitoraggio di impianti fotovoltaici', 'Evaluación y monitorización de plantas fotovoltaicas')
t('Performance monitoring of photovoltaic portfolios against a data-driven peer baseline, underperformance detection, and engineering review of plant design from a background in PV construction and commissioning.',
  'Παρακολούθηση απόδοσης χαρτοφυλακίων φωτοβολταϊκών σε σύγκριση με ομοειδείς σταθμούς με βάση δεδομένα, ανίχνευση υποαπόδοσης και τεχνικός έλεγχος του σχεδιασμού σταθμών, με υπόβαθρο στην κατασκευή και θέση σε λειτουργία φωτοβολταϊκών.',
  'Monitoraggio delle prestazioni di portafogli fotovoltaici rispetto a un riferimento data-driven di impianti simili, rilevamento di sottoprestazioni e revisione ingegneristica del progetto d\'impianto, con esperienza in costruzione e messa in servizio di impianti FV.',
  'Monitorización del rendimiento de carteras fotovoltaicas frente a una referencia basada en datos de plantas comparables, detección de bajo rendimiento y revisión técnica del diseño de la planta, con experiencia en construcción y puesta en marcha de instalaciones FV.')
t('Applied machine learning for energy', 'Εφαρμοσμένη μηχανική μάθηση για την ενέργεια', 'Machine learning applicato all\'energia', 'Aprendizaje automático aplicado a la energía')
t('Model development and review in Python, PyTorch and gradient boosting: data pipelines, feature design, validation protocols and production deployment with Docker and time-series databases.',
  'Ανάπτυξη και έλεγχος μοντέλων σε Python, PyTorch και gradient boosting: ροές δεδομένων, σχεδιασμός χαρακτηριστικών, πρωτόκολλα επικύρωσης και παραγωγική εγκατάσταση με Docker και βάσεις χρονοσειρών.',
  'Sviluppo e revisione di modelli in Python, PyTorch e gradient boosting: pipeline di dati, progettazione delle feature, protocolli di validazione e messa in produzione con Docker e database di serie temporali.',
  'Desarrollo y revisión de modelos en Python, PyTorch y gradient boosting: pipelines de datos, diseño de variables, protocolos de validación y despliegue en producción con Docker y bases de datos de series temporales.')
t('Research and EU project support', 'Υποστήριξη έρευνας και έργων ΕΕ', 'Supporto a ricerca e progetti UE', 'Apoyo a la investigación y a proyectos de la UE')
t('Technical writing and review, Horizon Europe proposal development and work-package structuring, and reporting, drawing on experience coordinating European energy projects.',
  'Τεχνική συγγραφή και έλεγχος, ανάπτυξη προτάσεων Horizon Europe και δόμηση πακέτων εργασίας, και αναφορές, με εμπειρία συντονισμού ευρωπαϊκών ενεργειακών έργων.',
  'Scrittura e revisione tecnica, sviluppo di proposte Horizon Europe e strutturazione dei work package, e rendicontazione, con esperienza nel coordinamento di progetti energetici europei.',
  'Redacción y revisión técnica, desarrollo de propuestas Horizon Europe y estructuración de paquetes de trabajo, e informes, con experiencia en la coordinación de proyectos energéticos europeos.')
t('Training and workshops', 'Εκπαίδευση και εργαστήρια', 'Formazione e workshop', 'Formación y talleres')
t("Short courses for engineering teams on forecasting, optimization and machine learning in power systems, with worked examples on the participants' own data where possible.",
  'Σύντομα μαθήματα για ομάδες μηχανικών σε πρόβλεψη, βελτιστοποίηση και μηχανική μάθηση για συστήματα ηλεκτρικής ενέργειας, με λυμένα παραδείγματα στα δεδομένα των συμμετεχόντων όπου είναι δυνατόν.',
  'Corsi brevi per team di ingegneri su previsione, ottimizzazione e machine learning nei sistemi elettrici, con esempi svolti sui dati dei partecipanti dove possibile.',
  'Cursos breves para equipos de ingeniería sobre predicción, optimización y aprendizaje automático en sistemas eléctricos, con ejemplos resueltos sobre los datos de los participantes cuando sea posible.')
t('Independent technical review', 'Ανεξάρτητος τεχνικός έλεγχος', 'Revisione tecnica indipendente', 'Revisión técnica independiente')
t('Second opinion on forecasting or scheduling systems you are buying or building: methodology, validation, and whether the reported accuracy will translate into operating savings.',
  'Δεύτερη γνώμη για συστήματα πρόβλεψης ή προγραμματισμού που αγοράζετε ή αναπτύσσετε: μεθοδολογία, επικύρωση και κατά πόσο η δηλωμένη ακρίβεια θα μεταφραστεί σε λειτουργική εξοικονόμηση.',
  'Seconda opinione su sistemi di previsione o programmazione che state acquistando o costruendo: metodologia, validazione e se l\'accuratezza dichiarata si tradurrà in risparmi operativi.',
  'Segunda opinión sobre sistemas de predicción o programación que esté comprando o construyendo: metodología, validación y si la precisión declarada se traducirá en ahorros operativos.')
t('How it works', 'Πώς λειτουργεί', 'Come funziona', 'Cómo funciona')
t('Engagement', 'Συνεργασία', 'Collaborazione', 'Colaboración')
t('Scoping call', 'Αρχική κλήση', 'Call iniziale', 'Llamada inicial')
t('A short conversation on the problem, the data you have and what a good outcome looks like. No charge.',
  'Μια σύντομη συζήτηση για το πρόβλημα, τα δεδομένα που έχετε και το πώς μοιάζει ένα καλό αποτέλεσμα. Χωρίς χρέωση.',
  'Una breve conversazione sul problema, sui dati disponibili e su come si presenta un buon risultato. Senza costo.',
  'Una breve conversación sobre el problema, los datos de que dispone y cómo sería un buen resultado. Sin coste.')
t('Proposal', 'Πρόταση', 'Proposta', 'Propuesta')
t('A one-page scope with deliverables, timeline and a fixed price or a day rate, depending on the work.',
  'Ένα μονοσέλιδο πλαίσιο με παραδοτέα, χρονοδιάγραμμα και σταθερή τιμή ή ημερήσια αμοιβή, ανάλογα με την εργασία.',
  'Un documento di una pagina con deliverable, tempistiche e prezzo fisso o tariffa giornaliera, a seconda del lavoro.',
  'Un documento de una página con entregables, calendario y precio fijo o tarifa diaria, según el trabajo.')
t('Delivery', 'Παράδοση', 'Consegna', 'Entrega')
t('Weekly check-ins, code and documentation handed over at the end, and a closing session with your team.',
  'Εβδομαδιαίες ενημερώσεις, παράδοση κώδικα και τεκμηρίωσης στο τέλος και μια τελική συνεδρία με την ομάδα σας.',
  'Aggiornamenti settimanali, consegna di codice e documentazione a fine lavoro e una sessione conclusiva con il vostro team.',
  'Reuniones semanales de seguimiento, entrega del código y la documentación al final y una sesión de cierre con su equipo.')
t('Start a conversation', 'Ξεκινήστε μια συζήτηση', 'Iniziamo a parlarne', 'Empecemos a hablar')
t('Write with a few lines on your problem and I will reply with whether and how I can help.',
  'Γράψτε μου λίγες γραμμές για το πρόβλημά σας και θα απαντήσω αν και πώς μπορώ να βοηθήσω.',
  'Scrivetemi poche righe sul vostro problema e vi risponderò se e come posso aiutare.',
  'Escríbame unas líneas sobre su problema y le responderé si puedo ayudar y cómo.')
t('Consulting and technical services by Marios Saleptsis: energy forecasting, battery scheduling and optimization, PV monitoring, applied machine learning.',
  'Συμβουλευτικές και τεχνικές υπηρεσίες του Μάριου Σαλέπτση: ενεργειακές προβλέψεις, προγραμματισμός και βελτιστοποίηση μπαταριών, παρακολούθηση φωτοβολταϊκών, εφαρμοσμένη μηχανική μάθηση.',
  'Servizi di consulenza e tecnici di Marios Saleptsis: previsione energetica, programmazione e ottimizzazione di batterie, monitoraggio fotovoltaico, machine learning applicato.',
  'Servicios de consultoría y técnicos de Marios Saleptsis: predicción energética, programación y optimización de baterías, monitorización fotovoltaica, aprendizaje automático aplicado.')

# Teaching
t('Teaching · Marios Saleptsis', 'Διδασκαλία · Marios Saleptsis', 'Didattica · Marios Saleptsis', 'Docencia · Marios Saleptsis')
t('Circuits and electric energy conversion', 'Κυκλώματα και ηλεκτρική μετατροπή ενέργειας', 'Circuiti e conversione elettrica dell\'energia', 'Circuitos y conversión eléctrica de la energía')
t('I teach at Politecnico di Milano as a teaching assistant on two master-level courses, and tutor seminars on AI and machine learning for power systems. My solutions are written the way I wish mine had been: theory first, then every number substituted before the result.',
  'Διδάσκω στο Politecnico di Milano ως βοηθός διδασκαλίας σε δύο μεταπτυχιακά μαθήματα και είμαι tutor σε σεμινάρια τεχνητής νοημοσύνης και μηχανικής μάθησης για συστήματα ηλεκτρικής ενέργειας. Οι λύσεις μου γράφονται όπως θα ήθελα να ήταν οι δικές μου: πρώτα η θεωρία, μετά κάθε αριθμός αντικατεστημένος πριν από το αποτέλεσμα.',
  'Insegno al Politecnico di Milano come assistente alla didattica in due corsi magistrali e seguo seminari su IA e machine learning per i sistemi elettrici. Le mie soluzioni sono scritte come avrei voluto fossero le mie: prima la teoria, poi ogni numero sostituito prima del risultato.',
  'Enseño en el Politecnico di Milano como profesor asistente en dos asignaturas de máster y tutorizo seminarios sobre IA y aprendizaje automático para sistemas eléctricos. Mis soluciones están escritas como me habría gustado que fueran las mías: primero la teoría, luego cada número sustituido antes del resultado.')
t('Courses', 'Μαθήματα', 'Corsi', 'Asignaturas')
t('Since February 2025. Lecturer for the exercise part of the course: weekly lectures, course material and numerical exercise solving.',
  'Από τον Φεβρουάριο 2025. Διδάσκων του τμήματος ασκήσεων του μαθήματος: εβδομαδιαίες διαλέξεις, εκπαιδευτικό υλικό και επίλυση αριθμητικών ασκήσεων.',
  'Da febbraio 2025. Docente della parte esercitativa del corso: lezioni settimanali, materiale didattico e risoluzione di esercizi numerici.',
  'Desde febrero de 2025. Profesor de la parte de ejercicios de la asignatura: clases semanales, material docente y resolución de ejercicios numéricos.')
t('Since February 2025. Lecturer for the exercise part of the course: power electronics, static converters and electrical machines, including DC-DC converters, induction and synchronous machines, three-phase systems, transformers and diode rectifiers, with fully solved derivations.',
  'Από τον Φεβρουάριο 2025. Διδάσκων του τμήματος ασκήσεων του μαθήματος: ηλεκτρονικά ισχύος, στατικοί μετατροπείς και ηλεκτρικές μηχανές, συμπεριλαμβανομένων μετατροπέων DC-DC, ασύγχρονων και σύγχρονων μηχανών, τριφασικών συστημάτων, μετασχηματιστών και ανορθωτών με διόδους, με πλήρως λυμένες αναλύσεις.',
  'Da febbraio 2025. Docente della parte esercitativa del corso: elettronica di potenza, convertitori statici e macchine elettriche, inclusi convertitori DC-DC, macchine asincrone e sincrone, sistemi trifase, trasformatori e raddrizzatori a diodi, con derivazioni completamente svolte.',
  'Desde febrero de 2025. Profesor de la parte de ejercicios de la asignatura: electrónica de potencia, convertidores estáticos y máquinas eléctricas, incluidos convertidores DC-DC, máquinas de inducción y síncronas, sistemas trifásicos, transformadores y rectificadores de diodos, con desarrollos completamente resueltos.')
t('Supervision', 'Επίβλεψη', 'Supervisione', 'Supervisión')
t('Student projects', 'Φοιτητικές εργασίες', 'Progetti degli studenti', 'Proyectos de estudiantes')
t("I tutor seminars on AI and machine learning for power systems and supervise master's theses at MG²Lab on forecasting and energy management. A current project applies MLP forecasters trained with the SPO+ loss to EV charging load and PV generation inside a two-layer energy management system.",
  'Είμαι tutor σε σεμινάρια τεχνητής νοημοσύνης και μηχανικής μάθησης για συστήματα ηλεκτρικής ενέργειας και επιβλέπω διπλωματικές εργασίες στο MG²Lab πάνω στην πρόβλεψη και τη διαχείριση ενέργειας. Μια τρέχουσα εργασία εφαρμόζει προβλέπτες MLP εκπαιδευμένους με τη συνάρτηση SPO+ σε φορτίο φόρτισης ηλεκτρικών οχημάτων και φωτοβολταϊκή παραγωγή μέσα σε ένα σύστημα διαχείρισης ενέργειας δύο επιπέδων.',
  'Seguo seminari su IA e machine learning per i sistemi elettrici e supervisiono tesi magistrali al MG²Lab su previsione e gestione dell\'energia. Un progetto in corso applica previsori MLP addestrati con la perdita SPO+ al carico di ricarica dei veicoli elettrici e alla produzione fotovoltaica all\'interno di un sistema di gestione dell\'energia a due livelli.',
  'Tutorizo seminarios sobre IA y aprendizaje automático para sistemas eléctricos y dirijo trabajos de fin de máster en el MG²Lab sobre predicción y gestión de energía. Un proyecto en curso aplica predictores MLP entrenados con la pérdida SPO+ a la carga de recarga de vehículos eléctricos y a la generación fotovoltaica dentro de un sistema de gestión de energía de dos niveles.')
t('If you are a PoliMi student interested in a thesis on forecasting, optimization or decision-focused learning for microgrids, write to me.',
  'Αν είστε φοιτητής του PoliMi και σας ενδιαφέρει διπλωματική σε πρόβλεψη, βελτιστοποίηση ή μάθηση προσανατολισμένη στην απόφαση για μικροδίκτυα, γράψτε μου.',
  'Se sei uno studente del PoliMi interessato a una tesi su previsione, ottimizzazione o decision-focused learning per microreti, scrivimi.',
  'Si eres estudiante del PoliMi y te interesa un TFM sobre predicción, optimización o aprendizaje orientado a la decisión para microrredes, escríbeme.')
t('Teaching by Marios Saleptsis at Politecnico di Milano: circuits and electric energy conversion.',
  'Διδασκαλία του Μάριου Σαλέπτση στο Politecnico di Milano: κυκλώματα και ηλεκτρική μετατροπή ενέργειας.',
  'Didattica di Marios Saleptsis al Politecnico di Milano: circuiti e conversione elettrica dell\'energia.',
  'Docencia de Marios Saleptsis en el Politecnico di Milano: circuitos y conversión eléctrica de la energía.')

# CV
t('CV · Marios Saleptsis', 'Βιογραφικό · Marios Saleptsis', 'CV · Marios Saleptsis', 'CV · Marios Saleptsis')
t('Curriculum vitae', 'Βιογραφικό σημείωμα', 'Curriculum vitae', 'Currículum vitae')
t('Electrical engineer working on forecasting, optimization and decision-focused learning for microgrids and battery storage.',
  'Ηλεκτρολόγος μηχανικός με αντικείμενο την πρόβλεψη, τη βελτιστοποίηση και τη μάθηση προσανατολισμένη στην απόφαση για μικροδίκτυα και αποθήκευση σε μπαταρίες.',
  'Ingegnere elettrico che si occupa di previsione, ottimizzazione e decision-focused learning per microreti e accumulo a batteria.',
  'Ingeniero eléctrico dedicado a la predicción, la optimización y el aprendizaje orientado a la decisión para microrredes y almacenamiento en baterías.')
t('Experience', 'Εμπειρία', 'Esperienza', 'Experiencia')
t('Positions', 'Θέσεις', 'Posizioni', 'Puestos')
t('Nov 2023 to present', 'Νοέ 2023 έως σήμερα', 'Nov 2023 a oggi', 'Nov 2023 a hoy')
t('Doctoral Researcher, Politecnico di Milano', 'Διδακτορικός ερευνητής, Politecnico di Milano', 'Dottorando di ricerca, Politecnico di Milano', 'Investigador doctoral, Politecnico di Milano')
t('Researcher on national and European funded projects aligned with the doctoral work: Centro Nazionale per la Mobilità Sostenibile (MOST), Management Energy Systems for Smart Island (MESSI) and Network for Energy Sustainable Technologies (NEST). Lead engineer for research and development in the forecasting division of DomOpti, a Politecnico di Milano spin-off. Lead member of the MG²Lab research team.',
  'Ερευνητής σε εθνικά και ευρωπαϊκά χρηματοδοτούμενα έργα συναφή με τη διδακτορική έρευνα: Centro Nazionale per la Mobilità Sostenibile (MOST), Management Energy Systems for Smart Island (MESSI) και Network for Energy Sustainable Technologies (NEST). Επικεφαλής μηχανικός έρευνας και ανάπτυξης στο τμήμα προβλέψεων της DomOpti, spin-off του Politecnico di Milano. Βασικό μέλος της ερευνητικής ομάδας του MG²Lab.',
  'Ricercatore su progetti finanziati nazionali ed europei allineati con il lavoro di dottorato: Centro Nazionale per la Mobilità Sostenibile (MOST), Management Energy Systems for Smart Island (MESSI) e Network for Energy Sustainable Technologies (NEST). Ingegnere responsabile di ricerca e sviluppo nella divisione previsioni di DomOpti, spin-off del Politecnico di Milano. Membro di riferimento del gruppo di ricerca MG²Lab.',
  'Investigador en proyectos financiados nacionales y europeos alineados con el trabajo doctoral: Centro Nazionale per la Mobilità Sostenibile (MOST), Management Energy Systems for Smart Island (MESSI) y Network for Energy Sustainable Technologies (NEST). Ingeniero responsable de investigación y desarrollo en la división de predicción de DomOpti, spin-off del Politecnico di Milano. Miembro principal del grupo de investigación MG²Lab.')
t('Sep 2025 to Feb 2026', 'Σεπ 2025 έως Φεβ 2026', 'Set 2025 a feb 2026', 'Sep 2025 a feb 2026')
t('Visiting Researcher, Polytechnique Montréal, Canada', 'Επισκέπτης ερευνητής, Polytechnique Montréal, Καναδάς', 'Ricercatore visitatore, Polytechnique Montréal, Canada', 'Investigador visitante, Polytechnique Montréal, Canadá')
t('Collaborative research on optimization and machine learning for decision-making in power systems, with a focus on end-to-end learning with gradient-based and gradient-free methods for the forecasting process in energy systems.',
  'Συνεργατική έρευνα σε βελτιστοποίηση και μηχανική μάθηση για τη λήψη αποφάσεων σε συστήματα ηλεκτρικής ενέργειας, με έμφαση στη μάθηση end-to-end με μεθόδους με και χωρίς κλίση για τη διαδικασία πρόβλεψης σε ενεργειακά συστήματα.',
  'Ricerca collaborativa su ottimizzazione e machine learning per il processo decisionale nei sistemi elettrici, con focus sull\'apprendimento end-to-end con metodi basati e non basati sul gradiente per il processo di previsione nei sistemi energetici.',
  'Investigación colaborativa en optimización y aprendizaje automático para la toma de decisiones en sistemas eléctricos, centrada en el aprendizaje end-to-end con métodos basados y no basados en gradiente para el proceso de predicción en sistemas energéticos.')
t('Feb 2025 to present', 'Φεβ 2025 έως σήμερα', 'Feb 2025 a oggi', 'Feb 2025 a hoy')
t("Lecturer on the master courses Electric Conversion from Green Sources of Energy and Fundamental Theory of Electric and Magnetic Circuits: course material, weekly lectures and numerical exercises on power electronics, static converters and electrical machines. Tutor on AI and machine learning for power systems seminars; master's thesis supervisor.",
  'Διδάσκων στα μεταπτυχιακά μαθήματα Electric Conversion from Green Sources of Energy και Fundamental Theory of Electric and Magnetic Circuits: εκπαιδευτικό υλικό, εβδομαδιαίες διαλέξεις και αριθμητικές ασκήσεις σε ηλεκτρονικά ισχύος, στατικούς μετατροπείς και ηλεκτρικές μηχανές. Tutor σε σεμινάρια τεχνητής νοημοσύνης και μηχανικής μάθησης για συστήματα ηλεκτρικής ενέργειας· επιβλέπων διπλωματικών εργασιών.',
  'Docente nei corsi magistrali Electric Conversion from Green Sources of Energy e Fundamental Theory of Electric and Magnetic Circuits: materiale didattico, lezioni settimanali ed esercizi numerici su elettronica di potenza, convertitori statici e macchine elettriche. Tutor nei seminari su IA e machine learning per i sistemi elettrici; relatore di tesi magistrali.',
  'Profesor en las asignaturas de máster Electric Conversion from Green Sources of Energy y Fundamental Theory of Electric and Magnetic Circuits: material docente, clases semanales y ejercicios numéricos sobre electrónica de potencia, convertidores estáticos y máquinas eléctricas. Tutor en seminarios de IA y aprendizaje automático para sistemas eléctricos; director de trabajos de fin de máster.')
t('Feb 2023 to Jan 2024', 'Φεβ 2023 έως Ιαν 2024', 'Feb 2023 a gen 2024', 'Feb 2023 a ene 2024')
t('EU Project Manager, Cluster of Bioeconomy and Environment, Greece', 'Διαχειριστής έργων ΕΕ, Cluster Βιοοικονομίας και Περιβάλλοντος, Ελλάδα', 'Project Manager UE, Cluster of Bioeconomy and Environment, Grecia', 'Gestor de proyectos UE, Cluster of Bioeconomy and Environment, Grecia')
t('Coordinated Horizon Europe research projects on renewable energy and advanced energy systems: cross-national partner collaboration, timelines and funding compliance. Proposal development, work-package structuring and periodic technical and budgetary reporting.',
  'Συντονισμός ερευνητικών έργων Horizon Europe για τις ανανεώσιμες πηγές ενέργειας και τα προηγμένα ενεργειακά συστήματα: συνεργασία διακρατικών εταίρων, χρονοδιαγράμματα και συμμόρφωση χρηματοδότησης. Ανάπτυξη προτάσεων, δόμηση πακέτων εργασίας και περιοδικές τεχνικές και οικονομικές αναφορές.',
  'Coordinamento di progetti di ricerca Horizon Europe su energie rinnovabili e sistemi energetici avanzati: collaborazione tra partner internazionali, tempistiche e conformità ai finanziamenti. Sviluppo di proposte, strutturazione dei work package e rendicontazione tecnica e finanziaria periodica.',
  'Coordinación de proyectos de investigación Horizon Europe sobre energías renovables y sistemas energéticos avanzados: colaboración entre socios internacionales, calendarios y cumplimiento de la financiación. Desarrollo de propuestas, estructuración de paquetes de trabajo e informes técnicos y presupuestarios periódicos.')
t('Nov 2020 to Sep 2021', 'Νοέ 2020 έως Σεπ 2021', 'Nov 2020 a set 2021', 'Nov 2020 a sep 2021')
t('Electrical Project Engineer, EcoEnergy SA, Greece', 'Ηλεκτρολόγος μηχανικός έργων, EcoEnergy SA, Ελλάδα', 'Ingegnere elettrico di progetto, EcoEnergy SA, Grecia', 'Ingeniero eléctrico de proyectos, EcoEnergy SA, Grecia')
t('Design, construction and commissioning of photovoltaic plants, combining office engineering with on-site supervision. Supply-chain coordination across projects, resolution of technical incidents and delivery on schedule and within budget.',
  'Σχεδιασμός, κατασκευή και θέση σε λειτουργία φωτοβολταϊκών σταθμών, συνδυάζοντας εργασία γραφείου με επίβλεψη στο εργοτάξιο. Συντονισμός εφοδιαστικής αλυσίδας σε πολλά έργα, επίλυση τεχνικών συμβάντων και παράδοση εντός χρονοδιαγράμματος και προϋπολογισμού.',
  'Progettazione, costruzione e messa in servizio di impianti fotovoltaici, combinando ingegneria d\'ufficio e supervisione in cantiere. Coordinamento della catena di fornitura su più progetti, risoluzione di incidenti tecnici e consegna nei tempi e nel budget.',
  'Diseño, construcción y puesta en marcha de plantas fotovoltaicas, combinando ingeniería de oficina con supervisión en obra. Coordinación de la cadena de suministro en varios proyectos, resolución de incidencias técnicas y entrega en plazo y dentro del presupuesto.')
t('Education', 'Εκπαίδευση', 'Formazione', 'Formación')
t('Degrees', 'Τίτλοι σπουδών', 'Titoli di studio', 'Titulaciones')
t('Nov 2023 to Nov 2026', 'Νοέ 2023 έως Νοέ 2026', 'Nov 2023 a nov 2026', 'Nov 2023 a nov 2026')
t('PhD in Electrical Engineering, Politecnico di Milano', 'Διδακτορικό Ηλεκτρολόγου Μηχανικού, Politecnico di Milano', 'Dottorato di ricerca in Ingegneria Elettrica, Politecnico di Milano', 'Doctorado en Ingeniería Eléctrica, Politecnico di Milano')
t('XXXIX cycle. Machine-learning forecasting and optimization models for microgrid scheduling, integrating day-ahead PV, load and electricity price forecasting with MILP and LP scheduling under market, operational and physical constraints. Validated on the MG²Lab microgrid testbed. Thesis: Cost-Aware and Decision-Focused Forecasting for Battery Energy Storage Scheduling in Microgrids. Supervisors: Sonia Leva and Marco Mussetta. Defense expected November 2026.',
  '39ος κύκλος. Μοντέλα πρόβλεψης με μηχανική μάθηση και βελτιστοποίησης για τον προγραμματισμό μικροδικτύων, με ενσωμάτωση προβλέψεων day-ahead φωτοβολταϊκών, φορτίου και τιμών ηλεκτρικής ενέργειας σε προγραμματισμό MILP και LP υπό περιορισμούς αγοράς, λειτουργίας και φυσικού συστήματος. Επικύρωση στο πειραματικό μικροδίκτυο του MG²Lab. Διατριβή: Cost-Aware and Decision-Focused Forecasting for Battery Energy Storage Scheduling in Microgrids. Επιβλέποντες: Sonia Leva και Marco Mussetta. Υποστήριξη αναμένεται Νοέμβριο 2026.',
  'XXXIX ciclo. Modelli di previsione basati su machine learning e di ottimizzazione per la programmazione di microreti, integrando previsioni day-ahead di fotovoltaico, carico e prezzi dell\'energia con programmazione MILP e LP sotto vincoli di mercato, operativi e fisici. Validati sul banco prova della microrete MG²Lab. Tesi: Cost-Aware and Decision-Focused Forecasting for Battery Energy Storage Scheduling in Microgrids. Relatori: Sonia Leva e Marco Mussetta. Discussione prevista a novembre 2026.',
  'Ciclo XXXIX. Modelos de predicción con aprendizaje automático y de optimización para la programación de microrredes, integrando predicciones day-ahead de fotovoltaica, carga y precios de la electricidad con programación MILP y LP bajo restricciones de mercado, operativas y físicas. Validados en el banco de pruebas de la microrred MG²Lab. Tesis: Cost-Aware and Decision-Focused Forecasting for Battery Energy Storage Scheduling in Microgrids. Directores: Sonia Leva y Marco Mussetta. Defensa prevista en noviembre de 2026.')
t('Sep 2016 to Jun 2023', 'Σεπ 2016 έως Ιουν 2023', 'Set 2016 a giu 2023', 'Sep 2016 a jun 2023')
t('Diploma in Electrical and Computer Engineering, University of Western Macedonia, Greece',
  'Δίπλωμα Ηλεκτρολόγου Μηχανικού και Μηχανικού Υπολογιστών, Πανεπιστήμιο Δυτικής Μακεδονίας, Ελλάδα',
  'Laurea in Ingegneria Elettrica e Informatica, Università della Macedonia Occidentale, Grecia',
  'Título en Ingeniería Eléctrica e Informática, Universidad de Macedonia Occidental, Grecia')
t("Integrated master's degree, 300 ECTS, specializing in power systems within electrical and energy engineering and computer science.",
  'Ενιαίο πτυχίο επιπέδου master, 300 ECTS, με ειδίκευση στα συστήματα ηλεκτρικής ενέργειας στο πλαίσιο της ηλεκτρολογίας, της ενεργειακής μηχανικής και της επιστήμης υπολογιστών.',
  'Laurea magistrale a ciclo unico, 300 ECTS, con specializzazione in sistemi elettrici nell\'ambito dell\'ingegneria elettrica ed energetica e dell\'informatica.',
  'Máster integrado, 300 ECTS, con especialización en sistemas eléctricos dentro de la ingeniería eléctrica y energética y la informática.')
t('Sep 2021 to Feb 2022', 'Σεπ 2021 έως Φεβ 2022', 'Set 2021 a feb 2022', 'Sep 2021 a feb 2022')
t('Erasmus semester, Universidad Politécnica de Madrid, Spain', 'Εξάμηνο Erasmus, Universidad Politécnica de Madrid, Ισπανία', 'Semestre Erasmus, Universidad Politécnica de Madrid, Spagna', 'Semestre Erasmus, Universidad Politécnica de Madrid, España')
t('Hands-on work in the IoT Laboratory and the Renewable Energies Laboratory.', 'Πρακτική εργασία στο Εργαστήριο IoT και στο Εργαστήριο Ανανεώσιμων Πηγών Ενέργειας.', 'Attività pratica nel laboratorio IoT e nel laboratorio di energie rinnovabili.', 'Trabajo práctico en el Laboratorio de IoT y en el Laboratorio de Energías Renovables.')
t('Output', 'Παραγωγή', 'Produzione', 'Producción')
t('One journal article and six conference papers published, four journal manuscripts under review at Energy, Applied Energy, IEEE Transactions on Smart Grid and IEEE Transactions on Industry Applications, and two papers accepted at ELECTRIMACS 2026. Full list on the',
  'Ένα άρθρο σε περιοδικό και έξι άρθρα συνεδρίων δημοσιευμένα, τέσσερα χειρόγραφα υπό κρίση στα Energy, Applied Energy, IEEE Transactions on Smart Grid και IEEE Transactions on Industry Applications, και δύο άρθρα αποδεκτά στο ELECTRIMACS 2026. Πλήρης κατάλογος στη',
  'Un articolo su rivista e sei articoli di conferenza pubblicati, quattro manoscritti in revisione presso Energy, Applied Energy, IEEE Transactions on Smart Grid e IEEE Transactions on Industry Applications, e due articoli accettati a ELECTRIMACS 2026. Elenco completo nella',
  'Un artículo de revista y seis artículos de congreso publicados, cuatro manuscritos en revisión en Energy, Applied Energy, IEEE Transactions on Smart Grid e IEEE Transactions on Industry Applications, y dos artículos aceptados en ELECTRIMACS 2026. Lista completa en la')
t('Research page', 'σελίδα Έρευνας', 'pagina Ricerca', 'página de Investigación')
t('Skills', 'Δεξιότητες', 'Competenze tecniche', 'Competencias')
t('Methods, tools and languages', 'Μέθοδοι, εργαλεία και γλώσσες', 'Metodi, strumenti e lingue', 'Métodos, herramientas e idiomas')
t('AI modelling for power systems', 'Μοντελοποίηση με τεχνητή νοημοσύνη για συστήματα ηλεκτρικής ενέργειας', 'Modellazione IA per sistemi elettrici', 'Modelado con IA para sistemas eléctricos')
t('Forecasting: PV, load, electricity prices', 'Πρόβλεψη: φωτοβολταϊκά, φορτίο, τιμές ηλεκτρικής ενέργειας', 'Previsione: fotovoltaico, carico, prezzi dell\'energia', 'Predicción: fotovoltaica, carga, precios de la electricidad')
t('Day-ahead electricity market', 'Αγορά ηλεκτρικής ενέργειας day-ahead', 'Mercato elettrico del giorno prima', 'Mercado eléctrico diario')
t('Decision-focused learning and optimization', 'Μάθηση προσανατολισμένη στην απόφαση και βελτιστοποίηση', 'Decision-focused learning e ottimizzazione', 'Aprendizaje orientado a la decisión y optimización')
t('Machine learning and optimization', 'Μηχανική μάθηση και βελτιστοποίηση', 'Machine learning e ottimizzazione', 'Aprendizaje automático y optimización')
t('Time-series and deep learning models', 'Μοντέλα χρονοσειρών και βαθιάς μάθησης', 'Modelli per serie temporali e deep learning', 'Modelos de series temporales y aprendizaje profundo')
t('MILP and LP formulations', 'Διατυπώσεις MILP και LP', 'Formulazioni MILP e LP', 'Formulaciones MILP y LP')
t('Programming and tools', 'Προγραμματισμός και εργαλεία', 'Programmazione e strumenti', 'Programación y herramientas')
t('Time-series databases, Grafana', 'Βάσεις χρονοσειρών, Grafana', 'Database di serie temporali, Grafana', 'Bases de datos de series temporales, Grafana')
t('Languages', 'Γλώσσες', 'Lingue', 'Idiomas')
t('Greek, native', 'Ελληνικά, μητρική', 'Greco, madrelingua', 'Griego, nativo')
t('English, C2', 'Αγγλικά, C2', 'Inglese, C2', 'Inglés, C2')
t('Italian, B1', 'Ιταλικά, B1', 'Italiano, B1', 'Italiano, B1')
t('Spanish, B1', 'Ισπανικά, B1', 'Spagnolo, B1', 'Español, B1')
t('Curriculum vitae of Marios Saleptsis, PhD in Electrical Engineering, Politecnico di Milano.',
  'Βιογραφικό σημείωμα του Μάριου Σαλέπτση, Διδάκτορα Ηλεκτρολόγου Μηχανικού, Politecnico di Milano.',
  'Curriculum vitae di Marios Saleptsis, dottore di ricerca in Ingegneria Elettrica, Politecnico di Milano.',
  'Currículum vitae de Marios Saleptsis, doctor en Ingeniería Eléctrica, Politecnico di Milano.')

# Offer card
t('Need forecasting, storage optimization or a second opinion on your energy project?',
  'Χρειάζεστε προβλέψεις, βελτιστοποίηση αποθήκευσης ή μια δεύτερη γνώμη για το ενεργειακό σας έργο;',
  'Vi serve una previsione, l\'ottimizzazione di un accumulo o una seconda opinione sul vostro progetto energetico?',
  '¿Necesita predicción, optimización de almacenamiento o una segunda opinión sobre su proyecto energético?')
t('Consulting and technical work, scoped as a short study, a delivered model or ongoing advisory. The first call is free.',
  'Συμβουλευτική και τεχνική εργασία, ως σύντομη μελέτη, παραδοτέο μοντέλο ή συνεχής συμβουλευτική. Η πρώτη κλήση είναι δωρεάν.',
  'Consulenza e lavoro tecnico, come studio breve, modello consegnato o consulenza continuativa. La prima call è gratuita.',
  'Consultoría y trabajo técnico, como estudio breve, modelo entregado o asesoría continuada. La primera llamada es gratuita.')
t('Get an offer', 'Ζητήστε προσφορά', 'Richiedi un\'offerta', 'Solicitar una oferta')

here = os.path.dirname(os.path.abspath(__file__))
for i, code in enumerate(['el', 'it', 'es'], start=1):
    json.dump({row[0]: row[i] for row in T}, open(os.path.join(here, code + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(T), 'strings')
