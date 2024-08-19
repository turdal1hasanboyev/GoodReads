# Dars rejasi

1. Django va Django Rest Framework larni o'rnatib oldik
    
2. O'zimizga kerak bo'lgan app larni ochib oldik
3. Modellar yozdik
4. Send email messages ni ko'rdik
5. User uchun Register API ishlab chiqdik
6. User uchun Login va VerifyEmail API ishlab chiqdik
7. Category uchun  CRUD API ishlab chiqdik
8. Article uchun CRUD API ishlab chiqdik
9. Review uchun CRUD API ishlab chiqdik
10. Award uchun CRUD API ishlab chiqdik
11. Book uchun CRUD API ishlab chiqdik
12. Request Friends uchun Follow, Unfollow va MyFriends API ishlab chiqdik.


# Class va Method lar

### GenericAPIView
- ListAPIView
- CreateAPIView
- RetrieveAPIView
- UpdateAPIView
- DestroyAPIView - bu faqat bazadagi ma'lumotni o'chiruvchi class, DELETE method ni qabul qiladi
- RetrieveUpdateDestroyAPIView - 3 ta class ni birlashtirgan class

### Useful methods

- get_queryset() - bu methodni override qilish orqali, queryset ni filter qilish mumkin
- select_related() - bu methodni override qilish orqali, queryset ni join qilish mumkin, foreign key bo'lgan fieldlarni bitta connection da olish uchun ishlatiladi
- prefetch_related() - bu methodni override qilish orqali, queryset ni join qilish mumkin, many to many fieldlarni bitta connection da olish uchun ishlatiladi
- get_permissions() - bu methodni override qilish orqali, permission ni o'zgartirish mumkin. Buni ko'proq Multiple class dan foydalanilganda ishlatildadi. Masalan, `IsAuthenticated` va `IsAuthor` permission larini bir vaqtda ishlatish uchun ishlatiladi

Serializerdan turib `request` dan ma'lumot olishni ko'rdik.
        
```python
def post(self, request, *args, **kwargs):
    context = {"user": request.user}
    serializer = self.get_serializer(data=request.data, context=context)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

# Keyingi darsda

## Studentlar uchun
- Genre va Award modellar uchun API ko'tarish

## O'qituvchi uchun
- API ni test lashni ko'ramiz ✅
- Qolgan modellar uchun API ko'tarishni davom etamiz! 🚶

#### Meme time 🕜:
- Backendchi bu - Frontni, Backni, Devopsdan oz-moz bilishi kerak va Tester lik qobiliyati ham bo'lishi kerak.
