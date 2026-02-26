"""
Script pour trouver la zone exacte de zoom correspondant au sujet.
"""
import numpy as np
from load_image import ft_load


def rgb_to_grayscale(image: np.ndarray, method: str = "red") -> np.ndarray:
    """
    Convertit une image RGB en niveaux de gris selon différentes méthodes.
    
    Args:
        image (np.ndarray): Image RGB (hauteur, largeur, 3).
        method (str): Méthode de conversion ("red", "green", "blue", "average", "weighted").
    
    Returns:
        np.ndarray: Image en niveaux de gris.
    """
    if method == "red":
        gray = image[:, :, 0:1]
    elif method == "green":
        gray = image[:, :, 1:2]
    elif method == "blue":
        gray = image[:, :, 2:3]
    elif method == "average":
        gray = np.mean(image, axis=2, keepdims=True)
    elif method == "weighted":
        gray = (0.299 * image[:, :, 0] +
                0.587 * image[:, :, 1] +
                0.114 * image[:, :, 2])
        gray = gray[:, :, np.newaxis]
    else:
        raise ValueError("Méthodes supportées: 'red', 'green', 'blue', 'average', 'weighted'")
    
    return gray.astype(np.uint8)


def test_zoom_zones(conversion_method="red"):
    """
    Teste différentes zones autour des valeurs approximatives trouvées visuellement.
    
    Args:
        conversion_method (str): Méthode de conversion RGB vers grayscale.
    """
    # Charger l'image
    image = ft_load("animal.jpeg")
    
    # Valeurs cibles du sujet
    target_first_pixels = [167, 180, 194]
    target_last_pixels = [102, 104, 103]
    
    print("=== RECHERCHE DE LA ZONE EXACTE ===")
    print(f"Méthode de conversion: {conversion_method}")
    print(f"Cibles début: {target_first_pixels}")
    print(f"Cibles fin: {target_last_pixels}")
    print()
    
    # Zone approximative trouvée visuellement
    base_h = 100
    base_w = 450
    
    # Tester dans un rayon autour de ces valeurs
    search_radius = 400
    zoom_size = 400
    
    best_matches = []
    
    for h_offset in range(-search_radius, search_radius + 1):
        for w_offset in range(-search_radius, search_radius + 1):
            start_h = base_h + h_offset
            start_w = base_w + w_offset
            
            # Vérifier que la zone reste dans l'image
            if (start_h < 0 or start_w < 0 or 
                start_h + zoom_size > image.shape[0] or 
                start_w + zoom_size > image.shape[1]):
                continue
            
            # Extraire la zone
            zone = image[start_h:start_h + zoom_size, start_w:start_w + zoom_size]
            
            # Convertir en grayscale selon la méthode choisie
            gray = rgb_to_grayscale(zone, method=conversion_method)
            
            # Premiers pixels
            first_pixels = [gray[0, 0, 0], gray[0, 1, 0], gray[0, 2, 0]]
            
            # Derniers pixels
            last_pixels = [gray[-3, -1, 0], gray[-2, -1, 0], gray[-1, -1, 0]]
            
            # Calculer la correspondance
            first_match = sum(1 for a, b in zip(first_pixels, target_first_pixels) if a == b)
            last_match = sum(1 for a, b in zip(last_pixels, target_last_pixels) if a == b)
            total_match = first_match + last_match
            
            if total_match > 0:  # Au moins une correspondance
                best_matches.append({
                    'start_h': start_h,
                    'start_w': start_w,
                    'method': conversion_method,
                    'first_pixels': first_pixels,
                    'last_pixels': last_pixels,
                    'first_match': first_match,
                    'last_match': last_match,
                    'total_match': total_match
                })
    
    # Trier par meilleure correspondance
    best_matches.sort(key=lambda x: x['total_match'], reverse=True)
    
    print("=== MEILLEURES CORRESPONDANCES ===")
    for i, match in enumerate(best_matches[:10]):  # Top 10
        print(f"\n{i+1}. Zone ({match['start_h']}, {match['start_w']}) - Méthode {match['method']}")
        print(f"   Premiers pixels: {match['first_pixels']} (match: {match['first_match']}/3)")
        print(f"   Derniers pixels: {match['last_pixels']} (match: {match['last_match']}/3)")
        print(f"   Score total: {match['total_match']}/6")
        
        # Si correspondance parfaite
        if match['total_match'] == 6:
            print(f"   ✅ CORRESPONDANCE PARFAITE TROUVÉE !")
            print(f"   Code à utiliser:")
            print(f"   start_h = {match['start_h']}")
            print(f"   start_w = {match['start_w']}")
            print(f"   Méthode: {match['method']}")
            break
    
    return best_matches


def test_specific_zone(start_h, start_w, conversion_method="red"):
    """
    Teste une zone spécifique en détail.
    """
    image = ft_load("animal.jpeg")
    
    print(f"\n=== TEST ZONE SPÉCIFIQUE ({start_h}, {start_w}) - Méthode {conversion_method} ===")
    
    # Extraire la zone
    zone = image[start_h:start_h + 400, start_w:start_w + 400]
    gray = rgb_to_grayscale(zone, method=conversion_method)
    
    # Afficher les premiers pixels (ligne par ligne)
    print("Premiers pixels:")
    for i in range(5):
        row_pixels = [gray[i, j, 0] for j in range(min(5, gray.shape[1]))]
        print(f"  Ligne {i}: {row_pixels}")
    
    # Afficher les derniers pixels
    print("Derniers pixels:")
    for i in range(-3, 0):
        row_pixels = [gray[i, j, 0] for j in range(-3, 0)]
        print(f"  Ligne {i}: {row_pixels}")
    
    return gray


def main():
    """
    Fonction principale de recherche.
    """
    try:
        print("🔍 RECHERCHE DE LA ZONE PARFAITE POUR LE ZOOM")
        print()
        
        # Choix de la méthode de conversion
        print("Méthodes de conversion disponibles:")
        methods = ["red", "green", "blue", "average", "weighted"]
        for i, method in enumerate(methods, 1):
            print(f"  {i}. {method}")
        
        while True:
            try:
                choice = input("\nChoisissez une méthode (1-5): ").strip()
                method_idx = int(choice) - 1
                if 0 <= method_idx < len(methods):
                    conversion_method = methods[method_idx]
                    break
                else:
                    print("❌ Choix invalide, veuillez entrer un nombre entre 1 et 5")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
        
        print(f"\n✅ Méthode sélectionnée: {conversion_method}")
        print()
        
        # Recherche automatique avec la méthode choisie
        matches = test_zoom_zones(conversion_method)
        
        # Test manuel d'une zone spécifique si besoin
        if input("\nTester une zone spécifique ? (y/n): ").lower() == 'y':
            h = int(input("start_h: "))
            w = int(input("start_w: "))
            test_specific_zone(h, w, conversion_method)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Recherche interrompue par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    main()